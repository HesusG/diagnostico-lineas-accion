#!/usr/bin/env python3
"""
Extractor de texto de PDFs y DOCX para el sistema de evaluación.
"""

import os
import sys
from pathlib import Path

try:
    import pdfplumber
except ImportError:
    print("Instalando pdfplumber...")
    os.system("pip install pdfplumber")
    import pdfplumber

try:
    from docx import Document
except ImportError:
    print("Instalando python-docx...")
    os.system("pip install python-docx")
    from docx import Document


def extract_pdf(filepath: str) -> str:
    """Extrae texto de un archivo PDF."""
    text_parts = []
    try:
        with pdfplumber.open(filepath) as pdf:
            for i, page in enumerate(pdf.pages):
                page_text = page.extract_text()
                if page_text:
                    text_parts.append(f"--- Página {i+1} ---\n{page_text}")
    except Exception as e:
        return f"ERROR al extraer PDF: {str(e)}"

    return "\n\n".join(text_parts) if text_parts else "ERROR: No se pudo extraer texto del PDF"


def extract_docx(filepath: str) -> str:
    """Extrae texto de un archivo DOCX."""
    try:
        doc = Document(filepath)
        paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
        return "\n\n".join(paragraphs) if paragraphs else "ERROR: Documento vacío"
    except Exception as e:
        return f"ERROR al extraer DOCX: {str(e)}"


def extract_document(filepath: str) -> str:
    """Extrae texto de un documento (PDF o DOCX)."""
    filepath = str(filepath)
    if filepath.lower().endswith('.pdf'):
        return extract_pdf(filepath)
    elif filepath.lower().endswith('.docx'):
        return extract_docx(filepath)
    else:
        return f"ERROR: Formato no soportado: {filepath}"


def process_all_documents(input_dir: str, output_dir: str) -> dict:
    """Procesa todos los documentos en el directorio de entrada."""
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    results = {}

    # Buscar archivos PDF y DOCX
    files = list(input_path.glob("*.pdf")) + list(input_path.glob("*.docx"))

    print(f"\nEncontrados {len(files)} archivos para procesar\n")

    for filepath in sorted(files):
        student_name = filepath.stem  # Nombre sin extensión
        print(f"Procesando: {student_name}...")

        # Extraer texto
        text = extract_document(str(filepath))

        # Guardar resultado
        output_file = output_path / f"{student_name}.txt"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(text)

        # Estadísticas
        word_count = len(text.split())
        char_count = len(text)
        has_error = text.startswith("ERROR")

        results[student_name] = {
            "file": str(filepath),
            "output": str(output_file),
            "words": word_count,
            "chars": char_count,
            "success": not has_error
        }

        status = "ERROR" if has_error else f"OK ({word_count} palabras)"
        print(f"  → {status}")

    return results


def main():
    # Rutas
    base_dir = Path(__file__).parent.parent
    input_dir = base_dir / "evidencia"
    output_dir = Path(__file__).parent / "output" / "extractions"

    print("=" * 60)
    print("EXTRACTOR DE DOCUMENTOS - Sistema de Evaluación")
    print("=" * 60)
    print(f"\nDirectorio de entrada: {input_dir}")
    print(f"Directorio de salida: {output_dir}")

    if not input_dir.exists():
        print(f"\nERROR: No existe el directorio de entrada: {input_dir}")
        sys.exit(1)

    results = process_all_documents(str(input_dir), str(output_dir))

    # Resumen
    print("\n" + "=" * 60)
    print("RESUMEN")
    print("=" * 60)

    successful = sum(1 for r in results.values() if r["success"])
    failed = len(results) - successful

    print(f"\nTotal procesados: {len(results)}")
    print(f"Exitosos: {successful}")
    print(f"Con errores: {failed}")

    if failed > 0:
        print("\nArchivos con errores:")
        for name, info in results.items():
            if not info["success"]:
                print(f"  - {name}")

    print(f"\nTextos extraídos guardados en: {output_dir}")

    return results


if __name__ == "__main__":
    main()
