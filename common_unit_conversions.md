## Collection of Common Unit Conversions

### Dose

Unit Conversions:

$$ Dose [nmol/kg] = Dose [mg/kg] * \left(  \frac{1 g}{1000 mg} \right) *  \left(  \frac{1}{MW [g/mol]} \right) *  \left(  \frac{10^9 nmol}{mol} \right) $$

$$ Dose [\mu mol/kg] = Dose [mg/kg] * \left(  \frac{1 g}{1000 mg} \right) *  \left(  \frac{1}{MW [g/mol]} \right) *  \left(  \frac{10^6 \mu mol}{mol} \right) $$

### Clearance

Unit Conversions:

$$ CL [L \cdot hr^{-1}\cdot  kg^{-1} ] = CL [mL \cdot min^{-1}\cdot  kg^{-1} ] * \left( \frac{ \text{L}}{1000 mL}\right) * \left( \frac{60 min}{hr}\right) $$

$$ CL [mL \cdot min^{-1}\cdot  kg^{-1} ]= CL [L \cdot hr^{-1}\cdot  kg^{-1} ]  * \left( \frac{ 1000 mL}{L}\right) * \left( \frac{hr}{60 min}\right) $$

Scaling:

$$CL_b = \frac{Q_h \cdot f_{u,b} \cdot CL_{int}}{Q_h + f_{u,b} \cdot CL_{int}}$$

Human CLint from microsomal stability assay:

$$CL_{int} \left[mL \cdot  min^{-1} \cdot kg^{-1} \right] = \underbrace{ \left(  \frac{\text{HLM} CL_{int,app} \left[\mu L \cdot  min^{-1} \cdot mg^{-1} \right]}{f_{u,mics}} \right) }_{\text{unbound} CL_{int,app} \text{from HLM}} * \overbrace{ \left( \frac{1 mL}{1000 \mu L} \right) }^{\text{unit conversion}} * \underbrace{ \left( \frac{32 mg}{1 g} \right) }_{\text{mg of protein per g of liver}} * \overbrace{ \left( \frac{25.7 g}{1 kg} \right) }^{\text{g of liver per kg of animal}}$$

Human CLint from hepatocyte stability assay:

$$CL_{int} \left[mL \cdot  min^{-1} \cdot kg^{-1} \right] = \underbrace{ \left(  \frac{\text{HHEP} CL_{int,app} \left[\mu L \cdot  min^{-1} \cdot million cells^{-1} \right]}{f_{u,heps}} \right) }_{\text{unbound} CL_{int,app} \text{from HHEP}} * \overbrace{ \left( \frac{1 mL}{1000 \mu L} \right) }^{\text{unit conversion}} * \underbrace{ \left( \frac{99 million cells}{1 g} \right) }_{\text{Hepatocellularity (million cells per g of liver)}} * \overbrace{ \left( \frac{25.7 g}{1 kg} \right) }^{\text{g of liver per kg of animal}}$$

Binding considerations:

$$BPR = \frac{f_{u,p}}{f_{u,b}}, \text{where} f_{u,matrix} = \frac{C_{u,matrix}}{C_{matrix}}$$

$$ \frac{CL_p}{CL_b} = BPR $$

$$ CL_u = \frac{CL_p}{f_{u,p}} $$

Definitions:

$$ CL_p = \frac{Dose_{IV}}{AUC_{p}}$$

$$ \frac{CL}{F} = \frac{Dose_{oral}}{AUC_{oral}}$$

$$ER = CL_b / Q_h$$

$$ t_{1 \slash 2} = \ln(2) * \frac{V_{ss}}{CL}, \text{where} \ln(2) \approx 0.693 $$

### Volume of Distribution

Unit Conversions:

$$ V_{ss} [L/kg] = V_{ss} [mL/kg] * \left(\frac{1000 mL}{L}\right) $$

$$ V_{ss} [mL/kg] = V_{ss} [L/kg] * \left( \frac{L}{1000 mL} \right) $$

Binding considerations:

$$BPR = \frac{f_{u,p}}{f_{u,b}}, \text{where} f_{u,matrix} = \frac{C_{u,matrix}}{C_{matrix}}$$

$$ \frac{V_p}{V_b} = {BPR}$$

$$ V_u = \frac{V_{ss}}{f_{u,p}}$$


Definitions:

$$ V_0 [L/kg] = \frac{Dose [mg/kg]}{C_0 [ng/mL]} * \left( \frac{10^{6} ng}{mg} \right) *  \left( \frac{1 L}{1000 mL} \right) $$

$$ t_{1 \slash 2} = \ln(2) * \frac{V_{d,ss}}{CL}, \text{where} \ln(2) \approx 0.693 $$

### Bioavailability

Definitions:

$$ F = \frac{AUC_{oral} / Dose_{oral}}{AUC_{IV} / Dose_{IV}} $$

$$ F = F_a F_g F_h = F_a F_g \left (1 - ER \right) = F_a F_g \left (1 - \frac{CL_b}{Q_h}\right) $$

### PK/PD

Unit Conversions

$$ C [\mu M] = C [ng/mL] * \left(\frac{1000 mL}{1 L}\right) * \left(\frac{1 \mu M}{1000 nM}\right) / MW [g/mol]$$

$$ C [ng/mL] = C [\mu M] * \left(\frac{1 L}{1000 mL}\right) * \left(\frac{1000 nM}{1 \mu M}\right) * MW [g/mol]$$

Binding considerations:

$$C_{u,assay} = C_{assay} * f_{u,assay}$$

$$C_{u,p} = C_p * f_{u,p}$$
