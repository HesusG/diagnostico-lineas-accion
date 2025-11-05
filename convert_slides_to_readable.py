#!/usr/bin/env python3
"""
Convert Slidev markdown to GitHub-readable markdown
Removes Slidev-specific syntax while preserving content
"""

import re
import sys

def convert_slidev_to_readable(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove YAML frontmatter
    content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)

    # Remove style imports
    content = re.sub(r'<style src=.*?</style>', '', content, flags=re.DOTALL)

    # Remove v-click divs and other Vue components
    content = re.sub(r'<div v-click[^>]*>', '', content)
    content = re.sub(r'<v-clicks>', '', content)
    content = re.sub(r'</v-clicks>', '', content)
    content = re.sub(r'<v-click[^>]*>', '', content)
    content = re.sub(r'</v-click>', '', content)
    content = re.sub(r'</div>(?:\s*\n)+(?=###|##|#|\*|-|```)', '\n\n', content)
    content = re.sub(r'</div>', '', content)

    # Remove other HTML divs with classes
    content = re.sub(r'<div class="[^"]*">', '', content)
    content = re.sub(r'<div>', '', content)

    # Remove layout and class directives (lines starting with layout: or class:)
    content = re.sub(r'^layout:.*\n', '', content, flags=re.MULTILINE)
    content = re.sub(r'^class:.*\n', '', content, flags=re.MULTILINE)

    # Convert slide separators (---) to section breaks with spacing
    # But preserve --- inside code blocks and mermaid
    lines = content.split('\n')
    result_lines = []
    in_code_block = False

    for line in lines:
        # Track code blocks
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            result_lines.append(line)
            continue

        # If it's just ---, convert to section break (but not in code blocks)
        if line.strip() == '---' and not in_code_block:
            result_lines.append('\n---\n')  # Keep as section divider
        else:
            result_lines.append(line)

    content = '\n'.join(result_lines)

    # Remove ::right:: and other slot markers
    content = re.sub(r'^::right::.*\n', '', content, flags=re.MULTILINE)

    # Clean up excessive blank lines (more than 2)
    content = re.sub(r'\n{4,}', '\n\n\n', content)

    # Remove ALL spans (including with attributes)
    content = re.sub(r'<span[^>]*>([^<]*)</span>', r'\1', content)
    content = re.sub(r'<span[^>]*>', '', content)

    # Remove remaining standalone closing tags
    content = re.sub(r'</span>', '', content)

    # Clean up remaining HTML tags (keep links and basic formatting)
    # But be careful not to remove code blocks
    content = re.sub(r'<br/?>', '\n', content)

    # Remove multiple consecutive --- (keep only one)
    content = re.sub(r'\n---\n\s*\n---\n', '\n---\n', content)

    # Remove <a> tags but keep href content for documentation links
    content = re.sub(r'<a href="([^"]*)"[^>]*>([^<]*)</a>', r'[\2](\1)', content)

    # Remove <small>, <strong> tags but keep content
    content = re.sub(r'<small>([^<]*)</small>', r'*\1*', content)
    content = re.sub(r'<strong>([^<]*)</strong>', r'**\1**', content)

    # Remove any other common HTML tags
    content = re.sub(r'</?(?:em|i)>', '*', content)
    content = re.sub(r'</?(?:b|strong)>', '**', content)

    # Clean up lines that are just whitespace
    lines = content.split('\n')
    cleaned_lines = [line if line.strip() else '' for line in lines]
    content = '\n'.join(cleaned_lines)

    # Remove excessive blank lines again after all cleaning
    content = re.sub(r'\n\n\n+', '\n\n', content)

    # Add header
    header = f"""# {output_file.split('/')[-1].replace('-readable.md', '').replace('-', ' ').title()}

> **Curso:** CD2001B - Diagnóstico para Líneas de Acción
> **Tecnológico de Monterrey - Campus Puebla**

---

"""

    content = header + content.strip()

    # Write output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✓ Converted: {input_file} → {output_file}")

if __name__ == '__main__':
    # Convert all slide files
    slides = [
        ('slides/semana1-medidas-descriptivas.md', 'slides/semana1-medidas-descriptivas-readable.md'),
        ('slides/semana1-pruebas-hipotesis.md', 'slides/semana1-pruebas-hipotesis-readable.md'),
        ('slides/semana2-chi-cuadrada-anova.md', 'slides/semana2-chi-cuadrada-anova-readable.md'),
        ('slides/semana2-regresion-correlacion.md', 'slides/semana2-regresion-correlacion-readable.md'),
    ]

    for input_file, output_file in slides:
        try:
            convert_slidev_to_readable(input_file, output_file)
        except Exception as e:
            print(f"✗ Error converting {input_file}: {e}")
