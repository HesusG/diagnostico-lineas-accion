# CODEBOOK: Fundación Esperanza - Donor Survey Dataset

**Dataset Name:** `fundacion_esperanza_donadores.csv`
**Version:** 1.0
**Date:** January 2025
**Purpose:** Educational dataset for statistical analysis training (CD2001B)
**Organization:** Fundación Esperanza (Fictional NGO - Health/Rehabilitation)
**Sample Size:** 1,000 donors
**Data Type:** Synthetic (generated for educational purposes)

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [Variable Descriptions](#variable-descriptions)
3. [Measurement Scales](#measurement-scales)
4. [Expected Correlations](#expected-correlations)
5. [Academic Justification](#academic-justification)
6. [Suggested Analyses](#suggested-analyses)
7. [References](#references)
8. [Limitations](#limitations)

---

## 1. Overview

### Dataset Description

This dataset contains survey responses from 1,000 donors to **Fundación Esperanza**, a fictional non-profit organization focused on health and rehabilitation services for children with disabilities (similar to Teletón Chile/Mexico).

The data captures:
- **Demographic characteristics** (age, education, income)
- **Donor behavior** (donation frequency, amount, years of support)
- **Attitudes and perceptions** (trust, satisfaction, emotional connection)
- **Future intentions** (likelihood to donate again)

### Research Context

The primary research question is: **What factors predict donor retention?**

This dataset is designed to teach statistical techniques covered in Weeks 1-2:
- Descriptive statistics
- t-tests (one-sample and two-sample)
- Chi-square test of independence
- One-way ANOVA
- Simple linear regression

### Ethical Considerations

⚠️ **IMPORTANT:** This is 100% synthetic data. No real donors, organizations, or personal information are represented. All data was generated using statistical simulation methods for educational purposes only.

---

## 2. Variable Descriptions

### 2.1 Demographic Variables

| Variable | Type | Values | Description |
|----------|------|--------|-------------|
| `edad_categoria` | Categorical | 18-25, 26-35, 36-45, 46-55, 56-65, 66+ | Age bracket of donor |
| `nivel_educacion` | Categorical | Secundaria, Técnico, Universitario, Postgrado | Highest education level completed |
| `rango_ingreso` | Categorical | <500k, 500k-1M, 1M-2M, 2M-4M, 4M+ | Monthly household income in Chilean pesos (CLP) |

**Interpretation Notes:**
- Age distribution reflects typical NGO donor demographics (peak 36-55 years)
- Education levels are higher than general population (donors tend to be more educated)
- Income brackets are self-reported estimates

---

### 2.2 Donor Behavior Variables

| Variable | Type | Values | Description |
|----------|------|--------|-------------|
| `tipo_donante` | Categorical | Individual, Empresa, Fundación | Type of donor entity |
| `frecuencia_donacion` | Categorical | Primera vez, Anual, Semestral, Trimestral, Mensual | Donation frequency |
| `canal_donacion` | Categorical | Teletón anual, Web, Transferencia, Presencial, Otro | Primary donation channel used |
| `participacion_eventos` | Categorical | Nunca, 1 vez, 2-3 veces, 4+ | Number of NGO events attended in past year |
| `voluntariado` | Binary | Sí, No | Has volunteered for the organization |
| `años_como_donante` | Numeric | 0-50 | Years as active donor (0 = first-time donor) |
| `monto_ultima_donacion` | Numeric | 5,000 - 10,000,000+ | Amount of last donation in CLP |

**Interpretation Notes:**
- `frecuencia_donacion` follows a pyramid structure (many first-time, few monthly)
- `tipo_donante = "Empresa"` typically has higher donation amounts
- `años_como_donante = 0` implies `frecuencia_donacion = "Primera vez"`
- `monto_ultima_donacion` follows a log-normal distribution (most small, few large)

---

### 2.3 Trust Dimensions (Likert Scale 1-10)

These variables measure different aspects of donor trust in the organization.

| Variable | Question (Spanish) | Scale |
|----------|-------------------|-------|
| `confianza_financiera` | "Confío en que la Fundación Esperanza usa las donaciones de manera eficiente y responsable" | 1 = Totalmente en desacuerdo<br>10 = Totalmente de acuerdo |
| `confianza_mision` | "Confío en que la Fundación está genuinamente comprometida con su misión" | 1-10 |
| `confianza_transparencia` | "La Fundación es transparente sobre cómo usa los fondos" | 1-10 |
| `confianza_liderazgo` | "Confío en el liderazgo y gestión de la Fundación" | 1-10 |

**Expected Distribution:**
- Mean: 7.0-7.3 (generally positive trust)
- SD: 1.7-1.9 (moderate variation)
- Skew: Slightly positive (few very low scores)

**Theoretical Basis:**
Trust is the strongest predictor of donor retention (Sargeant & Lee, 2004). Four dimensions are measured:
1. **Financial trust** - Efficient use of funds
2. **Mission trust** - Genuine commitment to cause
3. **Transparency** - Open communication about finances
4. **Leadership** - Confidence in management

---

### 2.4 Satisfaction Dimensions (Likert Scale 1-10)

These variables measure donor satisfaction with different organizational aspects.

| Variable | Question (Spanish) | Description |
|----------|-------------------|-------------|
| `satisfaccion_comunicacion` | "Estoy satisfecho con cómo la Fundación se comunica conmigo" | Quality/frequency of communication |
| `satisfaccion_impacto` | "Estoy satisfecho con la información de impacto que comparte la Fundación" | Impact reporting quality |
| `satisfaccion_reconocimiento` | "Me siento adecuadamente reconocido por mis contribuciones" | Donor recognition/acknowledgment |
| `satisfaccion_general` | "En general, estoy satisfecho con mi experiencia como donador" | Overall satisfaction composite |
| `satisfaccion_transparencia` | "Estoy satisfecho con la transparencia financiera de la Fundación" | Financial transparency satisfaction |

**Expected Distribution:**
- Mean: 6.8-7.1 (moderately high satisfaction)
- SD: 1.9-2.1 (more variation than trust)

**Theoretical Basis:**
Satisfaction mediates the relationship between organizational practices and donor retention (Bennett, 2003). Multiple satisfaction facets are measured because donors may be satisfied with some aspects but not others.

---

### 2.5 Engagement & Emotional Connection (Likert Scale 1-10)

These variables measure emotional and psychological bonds with the organization.

| Variable | Question (Spanish) | Construct |
|----------|-------------------|-----------|
| `conexion_emocional` | "Me siento emocionalmente conectado con la causa de la Fundación" | Emotional attachment to mission |
| `identificacion_mision` | "La misión de la Fundación se alinea con mis valores personales" | Value alignment |
| `orgullo_donante` | "Me siento orgulloso de ser donador de la Fundación" | Pride in association |
| `compromiso_futuro` | "Estoy comprometido a seguir apoyando a la Fundación en el futuro" | Future commitment intent |

**Expected Distribution:**
- Mean: 7.2-7.5 (high engagement for active donors)
- SD: 1.8-2.0

**Theoretical Basis:**
Emotional connection is a powerful predictor of long-term donor loyalty (Merchant et al., 2010). Donors with strong emotional bonds are less price-sensitive and more likely to increase donations over time.

---

### 2.6 Impact Perception (Likert Scale 1-10)

These variables measure perceived effectiveness and impact.

| Variable | Question (Spanish) | Focus |
|----------|-------------------|-------|
| `percepcion_impacto` | "Creo que mi donación hace una diferencia real" | Personal efficacy |
| `percepcion_eficacia` | "La Fundación aborda efectivamente las necesidades de personas con discapacidad" | Organizational effectiveness |

**Expected Distribution:**
- Mean: 7.3-7.4 (high perceived impact)
- SD: 1.8-1.9

**Theoretical Basis:**
Perceived impact directly influences donation decisions (Sargeant, 2001). Donors need to believe their contribution makes a tangible difference.

---

### 2.7 Target Variable (Outcome)

| Variable | Type | Values | Description |
|----------|------|--------|-------------|
| `donara_proximo_año` | Binary | Sí, No | Will the donor contribute again next year? |

**Distribution:**
- Sí (Yes): ~60% (realistic retention rate for established NGOs)
- No: ~40%

**Generation Method:**
This outcome was generated using a logistic regression model with predictors:
- `satisfaccion_general` (β = 0.40)
- `conexion_emocional` (β = 0.35)
- `confianza_financiera` (β = 0.25)
- `años_como_donante` (β = 0.20)

Plus random noise to simulate real-world unpredictability (life circumstances, economic changes, etc.).

---

## 3. Measurement Scales

### Likert Scale Interpretation (1-10)

| Score Range | Interpretation | Example |
|-------------|----------------|---------|
| 1-3 | **Very Low / Strongly Disagree** | Fundamental problems, likely to leave |
| 4-5 | **Low / Disagree** | Dissatisfaction present, at-risk donor |
| 6-7 | **Moderate / Somewhat Agree** | Neutral to slightly positive |
| 8-9 | **High / Agree** | Satisfied, likely to continue |
| 10 | **Very High / Strongly Agree** | Highly engaged, advocate |

### Why 1-10 Scale?

- More nuanced than traditional 1-5 Likert
- Allows detection of subtle differences in attitudes
- Closer to continuous data (better for regression analysis)
- Common in Latin American surveys

---

## 4. Expected Correlations

### 4.1 Correlation Matrix (Key Relationships)

Based on donor retention literature, the following correlations are expected:

| Variable 1 | Variable 2 | Expected r | Interpretation |
|-----------|-----------|-----------|----------------|
| `confianza_financiera` | `confianza_mision` | 0.65-0.75 | Trust dimensions intercorrelate |
| `confianza_financiera` | `satisfaccion_general` | 0.60-0.70 | Trust drives satisfaction |
| `conexion_emocional` | `compromiso_futuro` | 0.70-0.80 | Emotional bond predicts commitment |
| `percepcion_impacto` | `percepcion_eficacia` | 0.65-0.75 | Impact perceptions align |
| `satisfaccion_general` | `donara_proximo_año` | 0.50-0.65 | Satisfaction predicts retention |
| `años_como_donante` | `confianza_mision` | 0.40-0.55 | Tenure builds trust |
| `voluntariado` | `conexion_emocional` | 0.50-0.65 | Volunteers more emotionally connected |

### 4.2 Why These Correlations?

**Trust → Satisfaction (r ≈ 0.65-0.70)**
- Sargeant & Lee (2004) found trust is a primary driver of satisfaction
- Donors who trust an organization feel satisfied with their giving experience

**Emotional Connection → Future Commitment (r ≈ 0.75)**
- Merchant et al. (2010) showed emotional attachment is the strongest predictor of loyalty
- More powerful than satisfaction alone

**Satisfaction → Retention (r ≈ 0.55-0.60)**
- Bennett (2003) meta-analysis found moderate-to-strong correlation
- Not perfect because external factors (income changes, life events) also matter

**Years as Donor → Trust (r ≈ 0.45-0.50)**
- Relationship fundraising theory: trust builds over repeated positive interactions
- Long-term donors have observed consistent organizational behavior

---

## 5. Academic Justification

### 5.1 Theoretical Framework

This dataset is grounded in **Relationship Fundraising Theory** (Burnett, 2002), which posits that donor retention depends on:

1. **Trust** - Confidence in organizational integrity and competence
2. **Commitment** - Psychological attachment to the organization
3. **Satisfaction** - Positive experiences with the organization
4. **Communication Quality** - Timely, relevant, transparent information

These constructs form the foundation of the **Commitment-Trust Theory** (Morgan & Hunt, 1994), adapted for nonprofit contexts by Sargeant & Lee (2004).

### 5.2 Why These Variables Matter for NGO Practice

**For Fundraisers:**
- Identifies **actionable levers** (improve communication → increase satisfaction → boost retention)
- Segments donors by characteristics (e.g., volunteers vs. non-volunteers)
- Predicts churn risk (donors with low satisfaction/trust)

**For Strategists:**
- Informs resource allocation (which channels generate highest satisfaction?)
- Guides program development (what drives emotional connection?)
- Benchmarks organizational performance (how do we compare to industry standards?)

### 5.3 Pedagogical Design Choices

**Effect Sizes:**
- Set to medium-to-large (d = 0.5-0.7, r = 0.5-0.7) for **pedagogical clarity**
- Real-world effects are often smaller (d = 0.2-0.4), but stronger effects help students learn statistical concepts without ambiguity

**Clean Data:**
- No missing values (simplifies Week 1-2 focus on statistical tests)
- Logical consistency enforced (first-time donors have años = 0)
- Clear group differences (easy to detect patterns)

**Realistic Distribution:**
- Retention rate ~60% matches NGO industry benchmarks (40-65%)
- Age distribution reflects actual donor demographics
- Income/education skewed toward higher levels (donor self-selection)

---

## 6. Suggested Analyses

### 6.1 For Week 1 (Basic Statistics)

**Exercise 1: Descriptive Statistics**
```
Research Question: What is the average satisfaction level among donors?
Technique: Mean, median, SD, IQR of satisfaccion_general
Interpretation: Is satisfaction generally high or low? How much variation exists?
```

**Exercise 2: One-Sample t-test**
```
Research Question: Is average trust significantly above neutral (7.0)?
Technique: t-test comparing confianza_financiera to μ₀ = 7.0
H₀: μ = 7.0 (neutral trust)
H₁: μ ≠ 7.0
```

**Exercise 3: Two-Sample t-test**
```
Research Question: Do volunteers have higher emotional connection than non-volunteers?
Technique: Independent samples t-test
Groups: voluntariado (Sí vs. No)
Outcome: conexion_emocional
Expected: Volunteers score ~1.5 points higher
```

**Exercise 4: Two-Sample t-test (Retention Focus)**
```
Research Question: Do retained donors (donara_proximo_año = Sí) have higher
                  satisfaction than those who will leave?
Technique: Independent samples t-test
Groups: donara_proximo_año (Sí vs. No)
Outcome: satisfaccion_general
Expected: Retained donors score ~1-2 points higher
```

---

### 6.2 For Week 2 (Advanced Statistics)

**Exercise 5: Chi-Square Test**
```
Research Question: Is donor type (Individual/Empresa/Fundación) independent of
                  donation frequency?
Technique: Chi-square test of independence
Variables: tipo_donante × frecuencia_donacion
Expected: Empresas more likely to donate regularly (Anual/Semestral)
```

**Exercise 6: One-Way ANOVA**
```
Research Question: Does communication satisfaction vary by donation channel?
Technique: ANOVA + Tukey post-hoc
Independent: canal_donacion (5 levels)
Dependent: satisfaccion_comunicacion
Expected: Web and Presencial highest; Otro lowest
Follow-up: Which specific channels differ significantly?
```

**Exercise 7: Simple Linear Regression**
```
Research Question: Can years as donor predict future commitment?
Technique: Simple linear regression
Predictor: años_como_donante
Outcome: compromiso_futuro
Expected: Positive relationship, R² ≈ 0.20-0.30
Interpretation: Each additional year increases commitment by ~X points
```

**Exercise 8: Multiple Regression (BONUS)**
```
Research Question: Which factors best predict retention?
Technique: Logistic regression
Predictors: satisfaccion_general, conexion_emocional, confianza_financiera
Outcome: donara_proximo_año
Expected: All three significant predictors
Model accuracy: 70-75%
```

---

### 6.3 Cross-Workshop Integration

**Comparative Question:**
```
How do findings from descriptive analysis (Week 1) and regression (Week 2)
complement each other in understanding donor retention?

Week 1 insight: Retained donors have higher satisfaction (t-test)
Week 2 insight: Satisfaction predicts retention controlling for other factors (regression)
Integration: Satisfaction matters, but it's not the only factor
```

---

## 7. References

### Key Literature on Donor Retention

**Sargeant, A., & Lee, S. (2004).** Trust and relationship commitment in the United Kingdom voluntary sector: Determinants of donor behavior. *Psychology & Marketing, 21*(8), 613-635.
- Seminal work on trust in nonprofit context
- Found trust is primary predictor of donor loyalty

**Bennett, R. (2003).** Factors underlying the inclination to donate to particular types of charity. *International Journal of Nonprofit and Voluntary Sector Marketing, 8*(1), 12-29.
- Meta-analysis of donor satisfaction drivers
- Satisfaction mediates organizational actions and retention

**Merchant, A., Ford, J. B., & Sargeant, A. (2010).** Charitable organizations' storytelling influence on donors' emotions and intentions. *Journal of Consumer Psychology, 20*(3), 283-295.
- Emotional connection through narrative
- Emotions stronger than rational appeals

**Bekkers, R., & Wiepking, P. (2011).** A literature review of empirical studies of philanthropy: Eight mechanisms that drive charitable giving. *Nonprofit and Voluntary Sector Quarterly, 40*(5), 924-973.
- Comprehensive review of 500+ studies
- Identifies key predictors of giving behavior

**Richardson, M., Abraham, C., & Bond, R. (2012).** Psychological correlates of university students' academic performance: A systematic review and meta-analysis. *Psychological Bulletin, 138*(2), 353-387.
- Meta-analysis methodology example
- Shows importance of multivariate prediction

**Sargeant, A. (2001).** Relationship fundraising: How to keep donors loyal. *Nonprofit Management and Leadership, 12*(2), 177-192.
- Relationship fundraising framework
- Lifetime value of donors

---

## 8. Limitations

### 8.1 Synthetic Data Limitations

⚠️ **This dataset is 100% synthetic. Important caveats:**

1. **Simplified Relationships**
   - Linear correlations only (no interaction effects or non-linear patterns)
   - Stronger effect sizes than typical real-world data (pedagogical emphasis)
   - Perfect logical consistency (no data entry errors)

2. **No Missing Data**
   - Real surveys typically have 5-15% missing values
   - Missing data handling is not taught in Weeks 1-2

3. **Cross-Sectional Only**
   - No longitudinal component (all responses at one time point)
   - Cannot establish causality definitively
   - Cannot track donor behavior changes over time

4. **Uniform Measurement Error**
   - Real survey responses have heterogeneous reliability
   - Some respondents are less attentive than others

5. **Cultural Context**
   - Designed for Chilean/Latin American NGO context
   - May not generalize to other countries/cultures
   - Currency in Chilean pesos (CLP)

### 8.2 Appropriate Use

✅ **This dataset IS appropriate for:**
- Learning statistical techniques (t-tests, ANOVA, regression, chi-square)
- Understanding relationships between donor attitudes and behavior
- Practicing data analysis and interpretation
- Developing research questions and hypotheses
- Building statistical intuition

❌ **This dataset is NOT appropriate for:**
- Making real business decisions about actual NGOs
- Publishing as original research
- Claiming as real data collection
- Generalizing to specific organizations without validation

### 8.3 Transitioning to Real Data

After mastering techniques with this clean synthetic data, students should:
1. Work with messier real-world NGO data (Weeks 3-5)
2. Handle missing values, outliers, and inconsistencies
3. Deal with weaker, more ambiguous relationships
4. Make decisions under uncertainty

---

## 9. Dataset Generation

### 9.1 How Was This Data Created?

**Phase 1: Demographic Sampling**
- Age, education, income sampled from realistic distributions
- Donor type, frequency, channel based on NGO industry benchmarks
- Years as donor from exponential distribution (many new, few long-term)

**Phase 2: Likert Scale Generation**
- Base values from truncated normal distributions (μ=7.0-7.5, σ=1.8-2.0)
- Adjustments based on donor characteristics:
  - Volunteers: +1.5 points on engagement variables
  - Long-term donors: +0.5 points on trust variables
  - First-time donors: -1.0 points overall

**Phase 3: Correlation Structure**
- Multivariate adjustments to achieve target correlations
- Added noise (15-20%) for realism

**Phase 4: Target Variable**
- Logistic model: P(retain) = f(satisfaction, trust, engagement, tenure)
- Random noise added (donors don't follow models perfectly)
- Calibrated to achieve 60% retention rate

### 9.2 Reproducibility

- Random seed: 42
- Python 3.8+
- Libraries: numpy, pandas, scipy
- Generation script: `generator_ong_synthetic.py`

---

## 10. Version History

**v1.0 (January 2025)**
- Initial release
- 1,000 donors
- 26 variables
- Validated for distributional properties and correlations

---

## 11. Contact & Support

**Questions about this dataset?**
- Review suggested analyses above
- Check variable descriptions carefully
- Refer to referenced academic literature
- Consult course materials (Weeks 1-2 notebooks)

**Found an issue?**
- Dataset validation report: `validation_report.md`
- Generation script: `generator_ong_synthetic.py`

---

## 📊 Quick Variable Reference

```
DEMOGRAPHIC (3):    edad_categoria, nivel_educacion, rango_ingreso
DONOR TYPE (5):     tipo_donante, frecuencia_donacion, canal_donacion,
                    participacion_eventos, voluntariado
NUMERIC (2):        años_como_donante, monto_ultima_donacion
TRUST (4):          confianza_financiera, confianza_mision,
                    confianza_transparencia, confianza_liderazgo
SATISFACTION (5):   satisfaccion_comunicacion, satisfaccion_impacto,
                    satisfaccion_reconocimiento, satisfaccion_general,
                    satisfaccion_transparencia
ENGAGEMENT (4):     conexion_emocional, identificacion_mision,
                    orgullo_donante, compromiso_futuro
IMPACT (2):         percepcion_impacto, percepcion_eficacia
TARGET (1):         donara_proximo_año
```

**Total: 26 variables**

---

*This codebook was created for educational purposes as part of CD2001B course materials.*
*Fundación Esperanza is a fictional organization. All data is synthetic.*
