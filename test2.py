import svgwrite

def generate_dot_grid_svg(
    dot_spacing_x=1,
    line_spacing_y=6,
    margin=15,
    paper_width=210,
    paper_height=297,
    dot_radius=0.5,
    dot_color='black',
    dot_opacity=1.0,
    file_name='dot_grid_paper.svg'
):
    # Create SVG drawing
    dwg = svgwrite.Drawing(file_name, size=(f"{paper_width}mm", f"{paper_height}mm"))

    # Calculate effective area
    effective_width = paper_width - 2 * margin
    effective_height = paper_height - 2 * margin

    # Generate dots with the specified color and opacity
    current_y = margin
    while current_y <= margin + effective_height:
        current_x = margin
        while current_x <= margin + effective_width:
            dwg.add(dwg.circle(center=(f"{current_x}mm", f"{current_y}mm"), r=f"{dot_radius}mm", fill=dot_color, fill_opacity=dot_opacity))
            current_x += dot_spacing_x
        current_y += line_spacing_y

    # Save the drawing
    dwg.save()
    return f"SVG file '{file_name}' generated successfully."

# User inputs
dot_spacing_x = float(input("Enter the spacing between dots (in mm): "))
line_spacing_y = float(input("Enter the spacing between lines (in mm): "))
margin = float(input("Enter the margin size (in mm): "))
paper_width = float(input("Enter the paper width (in mm): "))
paper_height = float(input("Enter the paper height (in mm): "))
dot_radius = float(input("Enter the dot radius (in mm): "))
dot_color = input("Enter the dot color (CSS color value): ")
dot_opacity = float(input("Enter the dot opacity (0.0 to 1.0): "))
file_name = input("Enter the output file name (with .svg extension): ")

# Generate the SVG
result = generate_dot_grid_svg(
    dot_spacing_x=dot_spacing_x,
    line_spacing_y=line_spacing_y,
    margin=margin,
    paper_width=paper_width,
    paper_height=paper_height,
    dot_radius=dot_radius,
    dot_color=dot_color,
    dot_opacity=dot_opacity,
    file_name=file_name
)

print(result)
