from fpdf import FPDF

class CapabilityPDF(FPDF):
    def header(self):
        logo_path = r'C:\Users\Jordyn\Desktop\LMT-CONTENT\04-ASSETS\01-IMAGES\logos\50techbridge-logo-transparent.png'
        self.image(logo_path, x=10, y=8, w=55)
        self.set_xy(70, 8)
        self.set_font('Helvetica', 'B', 16)
        self.set_text_color(30, 60, 120)
        self.cell(0, 8, 'LEARN MORE TECHNOLOGIES', new_x="LMARGIN", new_y="NEXT")
        self.set_x(70)
        self.set_font('Helvetica', 'B', 11)
        self.set_text_color(80, 80, 80)
        self.cell(0, 6, 'Capability Statement', new_x="LMARGIN", new_y="NEXT")
        self.set_y(28)
        self.set_draw_color(30, 60, 120)
        self.set_line_width(0.8)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(3)

    def section_header(self, title):
        self.set_font('Helvetica', 'B', 9)
        self.set_fill_color(30, 60, 120)
        self.set_text_color(255, 255, 255)
        self.cell(0, 5.5, '  ' + title, new_x="LMARGIN", new_y="NEXT", fill=True)
        self.set_text_color(0, 0, 0)
        self.ln(1.5)

    def body_text(self, text):
        self.set_font('Helvetica', '', 7.5)
        self.multi_cell(0, 3.5, text)
        self.ln(1)

    def bullet(self, text):
        self.set_font('Helvetica', '', 7.5)
        x = self.get_x()
        self.cell(4, 3.5, '-')
        self.multi_cell(0, 3.5, text)

    def bold_bullet(self, bold_part, rest):
        self.set_font('Helvetica', '', 7.5)
        self.cell(4, 3.5, '-')
        self.set_font('Helvetica', 'B', 7.5)
        self.write(3.5, bold_part)
        self.set_font('Helvetica', '', 7.5)
        self.write(3.5, rest)
        self.ln(4)

    def table_row(self, col1, col2, bold=False, header=False):
        if header:
            self.set_font('Helvetica', 'B', 7)
            self.set_fill_color(220, 230, 245)
            self.cell(55, 4.5, col1, border=1, fill=True)
            self.cell(0, 4.5, col2, border=1, new_x="LMARGIN", new_y="NEXT", fill=True)
        else:
            style = 'B' if bold else ''
            self.set_font('Helvetica', style, 7)
            self.cell(55, 4, col1, border='LR')
            self.set_font('Helvetica', '', 7)
            self.cell(0, 4, col2, border='LR', new_x="LMARGIN", new_y="NEXT")

pdf = CapabilityPDF('P', 'mm', 'Letter')
pdf.set_auto_page_break(auto=True, margin=10)
pdf.add_page()

# Contact info bar
pdf.set_font('Helvetica', '', 7)
pdf.set_text_color(60, 60, 60)
pdf.cell(0, 3.5, 'Brian McKinney, CEO  |  2724 Philomena St #433, Austin TX 78723  |  brian@learnmo.com  |  cal.com/brianmckinney', new_x="LMARGIN", new_y="NEXT", align='C')
pdf.cell(0, 3.5, 'learnmoretechnologies.com  |  50plustechbridge.com  |  MBE Certified  |  WIOA Eligible  |  SAM.gov Registered', new_x="LMARGIN", new_y="NEXT", align='C')
pdf.set_text_color(0, 0, 0)
pdf.ln(2)

# Two-column layout using cells
col_w = 92
gap = 6

# Save Y position for two-column start
y_start = pdf.get_y()

# LEFT COLUMN
pdf.set_xy(10, y_start)

# About
pdf.section_header('ABOUT')
pdf.set_font('Helvetica', '', 7.5)
pdf.multi_cell(col_w, 3.5,
    '50+TechBridge is the only program in America teaching AI skills specifically to adults 50+. '
    'We deliver free, hands-on AI and digital literacy workshops at public libraries, senior centers, '
    'and community organizations across Central Texas. Founded by Brian McKinney - a 65-year-old solo '
    'CEO who manages 30+ AI-powered workflows - we prove that age is not a barrier to innovation.')
pdf.ln(2)

# Core Competencies
pdf.set_x(10)
pdf.section_header('CORE COMPETENCIES')
comps = [
    'AI & Digital Literacy Training for Adults 50+',
    'Customized Curriculum Development',
    'Workshop Facilitation (Libraries, Senior Centers, Community Orgs)',
    'Free, Publicly Accessible Programming',
    'Digital Equity Advocacy & Workforce Development',
    'Content Production (Newsletter, Video, Podcast, Course)',
]
for c in comps:
    pdf.set_x(10)
    pdf.bullet(c)
pdf.ln(2)

# Past Performance
pdf.set_x(10)
pdf.section_header('PAST PERFORMANCE - GOVERNMENT GRANTS')
pdf.set_x(10)
pdf.set_font('Helvetica', 'B', 7.5)
pdf.multi_cell(col_w, 3.5, 'City of Austin Nexus Grant - 2024 (AACME)')
pdf.set_x(10)
pdf.set_font('Helvetica', '', 7.5)
pdf.multi_cell(col_w, 3.5,
    'Award: $5,000 | Status: Awarded & Delivered\n'
    'Scope: Digital skills workshops as publicly accessible creative technology and cultural programming. '
    'All post-award requirements completed: kick-off meeting, activity delivery, final report, marketing compliance.')
pdf.ln(2)

# Certifications
pdf.set_x(10)
pdf.section_header('CERTIFICATIONS & REGISTRATIONS')
certs = [
    'MBE Certified (Minority Business Enterprise)',
    'WIOA Eligible (Workforce Innovation & Opportunity Act)',
    'SAM.gov Registered | City of Austin Vendor',
    '501(c)(3) Filing: In progress (July 2026)',
]
for c in certs:
    pdf.set_x(10)
    pdf.bullet(c)
pdf.ln(2)

# NAICS
pdf.set_x(10)
pdf.section_header('NAICS CODES')
naics = [
    ('611430', 'Professional & Management Development Training'),
    ('611710', 'Educational Support Services'),
    ('611699', 'All Other Miscellaneous Schools & Instruction'),
    ('541611', 'Admin Management & General Mgmt Consulting'),
    ('541990', 'All Other Professional/Scientific/Technical Services'),
]
for code, desc in naics:
    pdf.set_x(10)
    pdf.set_font('Helvetica', 'B', 7)
    pdf.cell(12, 3.5, code)
    pdf.set_font('Helvetica', '', 7)
    pdf.cell(col_w - 12, 3.5, desc, new_x="LMARGIN", new_y="NEXT")

y_left_end = pdf.get_y()

# RIGHT COLUMN
pdf.set_xy(10 + col_w + gap, y_start)

# Performance Data
pdf.section_header('PERFORMANCE DATA (Verified)                          ')
metrics = [
    ('Adults trained', '264+'),
    ('In-person locations', '13'),
    ('Austin Public Library branches', '9'),
    ('Senior centers served', '3'),
    ('Veterans programs', '1 (Foundation Communities)'),
    ('Online learners (LearnDash)', '24'),
    ('AI-powered workflows', '30+'),
    ('Targeted completion rate', '3x industry average'),
]
pdf.set_x(10 + col_w + gap)
pdf.table_row('Metric', 'Number', header=True)
for m, n in metrics:
    pdf.set_x(10 + col_w + gap)
    pdf.table_row(m, n, bold=(m == 'Adults trained'))
# Close table bottom
pdf.set_x(10 + col_w + gap)
pdf.cell(55, 0, '', border='T')
pdf.cell(0, 0, '', border='T', new_x="LMARGIN", new_y="NEXT")
pdf.ln(3)

# Differentiators
pdf.set_x(10 + col_w + gap)
pdf.section_header('DIFFERENTIATORS                                      ')
diffs = [
    ('Only 50+ AI Program in America', ' - No other program targets this demographic with AI training'),
    ('Proven AACME Track Record', ' - 2024 Nexus grantee; understands ACME reporting & compliance'),
    ('Customized Curriculum', ' - Each partner org receives training tailored to their community'),
    ('Zero Cost to Participants', ' - All workshops free and publicly accessible'),
    ('Community-Embedded', ' - Delivered where people already gather'),
]
for bold, rest in diffs:
    pdf.set_x(10 + col_w + gap)
    pdf.bold_bullet(bold, rest)
pdf.ln(1)

# Partner Ecosystem
pdf.set_x(10 + col_w + gap)
pdf.section_header('PARTNER ECOSYSTEM                                    ')
pdf.set_x(10 + col_w + gap)
pdf.set_font('Helvetica', 'B', 7)
pdf.cell(col_w, 3.5, 'Active Partners:', new_x="LMARGIN", new_y="NEXT")
active = [
    'Austin Public Library (9 branches)',
    'Senior Activity Centers (Conley-Guerrero, Lamar, South Austin)',
    'Foundation Communities (Veterans program)',
]
for p in active:
    pdf.set_x(10 + col_w + gap)
    pdf.set_font('Helvetica', '', 7)
    pdf.bullet(p)

pdf.ln(1)
pdf.set_x(10 + col_w + gap)
pdf.set_font('Helvetica', 'B', 7)
pdf.cell(col_w, 3.5, 'Prospective:', new_x="LMARGIN", new_y="NEXT")
prospective = [
    'AGE of Central Texas',
    'Workforce Solutions Capital Area',
    'Austin Area Urban League',
    'Huston-Tillotson University',
]
for p in prospective:
    pdf.set_x(10 + col_w + gap)
    pdf.set_font('Helvetica', '', 7)
    pdf.bullet(p)
pdf.ln(2)

# Elevate Alignment
pdf.set_x(10 + col_w + gap)
pdf.section_header('ELEVATE GRANT ALIGNMENT                              ')
align_items = [
    ('2+ yrs Austin production', 'Active since 2024, 13 locations'),
    ('Publicly accessible', 'All workshops free & open'),
    ('Reflects Austin cultures', 'Serves diverse 50+ communities'),
    ('Prior AACME relationship', '2024 Nexus grant awardee'),
    ('Budget under $500K', 'Lean solo operation'),
]
pdf.set_x(10 + col_w + gap)
pdf.table_row('Elevate Criteria', '50+TechBridge Fit', header=True)
for c, f in align_items:
    pdf.set_x(10 + col_w + gap)
    pdf.table_row(c, f)
pdf.set_x(10 + col_w + gap)
pdf.cell(55, 0, '', border='T')
pdf.cell(0, 0, '', border='T', new_x="LMARGIN", new_y="NEXT")

# Footer
y_bottom = max(y_left_end, pdf.get_y()) + 5
pdf.set_xy(10, y_bottom)
pdf.set_draw_color(30, 60, 120)
pdf.set_line_width(0.5)
pdf.line(10, y_bottom, 200, y_bottom)
pdf.ln(2)
pdf.set_font('Helvetica', 'I', 7)
pdf.set_text_color(80, 80, 80)
pdf.cell(0, 3.5, '"Ageism is the problem. AI is the equalizer. We\'re the bridge."', new_x="LMARGIN", new_y="NEXT", align='C')
pdf.cell(0, 3.5, 'Brian McKinney  |  brian@learnmo.com  |  cal.com/brianmckinney  |  learnmoretechnologies.com', new_x="LMARGIN", new_y="NEXT", align='C')

output_path = r'C:\Users\Jordyn\Desktop\LMT-CONTENT\05-BUSINESS-OPS\07-GRANTS\ELEVATE-2026\LMT-Capability-Statement-Elevate-2026.pdf'
pdf.output(output_path)
print(f'PDF saved to: {output_path}')
