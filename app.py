
import streamlit as st
import pandas as pd
import datetime

# =====================================
# PAGE CONFIGURATION
# =====================================

st.set_page_config(
    page_title="Student Web Application",
    page_icon="📚",
    layout="wide"
)

# =====================================
# MAIN HEADER
# =====================================

st.header("Gerald Brandon A. Seriño")

st.title("📚 Student Productivity Dashboard")

st.write(
    "Welcome to my Streamlit Web Application! "
    "This application provides useful tools "
    "for students."
)

st.divider()

# =====================================
# SIDEBAR NAVIGATION
# =====================================

st.sidebar.title("📌 Navigation")

menu = st.sidebar.selectbox(
    "Choose a Tool",
    [
        "Home",
        "Simple Calculator",
        "To-Do List",
        "Notes",
        "Unit Converter",
        "About"
    ]
)

# =====================================
# HOME
# =====================================

if menu == "Home":

    st.subheader("🏠 Welcome!")

    st.write("""
    Welcome to my Student Productivity Dashboard.

    This application contains different tools
    designed to help students with their daily tasks.
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("🧮 Simple Calculator")

    with col2:
        st.info("📝 To-Do List")

    with col3:
        st.info("📏 Unit Converter")

    st.subheader("✨ Application Features")

    st.write("""
    - Simple Calculator
    - To-Do List
    - Personal Notes
    - Multiple Unit Conversions
    - About the Developer
    """)

# =====================================
# SIMPLE CALCULATOR
# =====================================

elif menu == "Simple Calculator":

    st.subheader("🧮 Simple Calculator")

    num1 = st.number_input(
        "Enter First Number",
        value=0.0
    )

    num2 = st.number_input(
        "Enter Second Number",
        value=0.0
    )

    operation = st.selectbox(
        "Select Operation",
        [
            "Addition",
            "Subtraction",
            "Multiplication",
            "Division",
            "Modulus",
            "Exponentiation"
        ]
    )

    if st.button("Calculate"):

        if operation == "Addition":
            result = num1 + num2

        elif operation == "Subtraction":
            result = num1 - num2

        elif operation == "Multiplication":
            result = num1 * num2

        elif operation == "Division":
            if num2 == 0:
                st.error("Cannot divide by zero!")
                result = None
            else:
                result = num1 / num2

        elif operation == "Modulus":
            if num2 == 0:
                st.error("Cannot divide by zero!")
                result = None
            else:
                result = num1 % num2

        elif operation == "Exponentiation":
            result = num1 ** num2

        if result is not None:
            st.success(f"Result: {result}")

# =====================================
# TO-DO LIST
# =====================================

elif menu == "To-Do List":

    st.subheader("📝 My To-Do List")

    if "tasks" not in st.session_state:
        st.session_state.tasks = []

    task = st.text_input("Enter a new task")

    if st.button("Add Task"):

        if task.strip():
            st.session_state.tasks.append({
                "task": task.strip(),
                "done": False
            })

            st.success("Task added successfully!")

        else:
            st.warning("Please enter a task.")

    st.write("### Your Tasks")

    for i, item in enumerate(st.session_state.tasks):

        col1, col2 = st.columns([4, 1])

        with col1:
            st.checkbox(
                item["task"],
                value=item["done"],
                key=f"task_{i}",
                on_change=lambda index=i: (
                    st.session_state.tasks[index].update(
                        {"done": st.session_state[f"task_{index}"]}
                    )
                )
            )

        with col2:
            if st.button("🗑️", key=f"delete_{i}"):
                st.session_state.tasks.pop(i)
                st.rerun()

    if st.button("Clear All Tasks"):
        st.session_state.tasks = []
        st.rerun()

# =====================================
# PERSONAL NOTES
# =====================================

elif menu == "Notes":

    st.subheader("📒 Personal Notes")

    if "saved_notes" not in st.session_state:
        st.session_state.saved_notes = ""

    note = st.text_area(
        "Write your notes here",
        value=st.session_state.saved_notes,
        height=200
    )

    if st.button("Save Notes"):

        st.session_state.saved_notes = note

        st.success("Notes saved successfully!")

    if st.button("Clear Notes"):

        st.session_state.saved_notes = ""

        st.success("Notes cleared!")

        st.rerun()

# =====================================
# UNIT CONVERTER
# =====================================

elif menu == "Unit Converter":

    st.subheader("📏 Multiple Unit Converter")

    category = st.selectbox(
        "Select Conversion Category",
        [
            "Length",
            "Weight",
            "Temperature",
            "Time",
            "Area",
            "Volume",
            "Speed",
            "Data Storage"
        ]
    )

    # LENGTH
    if category == "Length":

        units = {
            "Kilometers": 1000,
            "Meters": 1,
            "Centimeters": 0.01,
            "Millimeters": 0.001,
            "Miles": 1609.344,
            "Yards": 0.9144,
            "Feet": 0.3048,
            "Inches": 0.0254
        }

    # WEIGHT
    elif category == "Weight":

        units = {
            "Kilograms": 1,
            "Grams": 0.001,
            "Milligrams": 0.000001,
            "Metric Tons": 1000,
            "Pounds": 0.45359237,
            "Ounces": 0.0283495
        }

    # TIME
    elif category == "Time":

        units = {
            "Seconds": 1,
            "Minutes": 60,
            "Hours": 3600,
            "Days": 86400,
            "Weeks": 604800,
            "Months (30 days)": 2592000,
            "Years (365 days)": 31536000
        }

    # AREA
    elif category == "Area":

        units = {
            "Square Meters": 1,
            "Square Kilometers": 1000000,
            "Square Centimeters": 0.0001,
            "Hectares": 10000,
            "Acres": 4046.8564224,
            "Square Feet": 0.09290304,
            "Square Inches": 0.00064516
        }

    # VOLUME
    elif category == "Volume":

        units = {
            "Liters": 1,
            "Milliliters": 0.001,
            "Cubic Meters": 1000,
            "Gallons (US)": 3.785411784,
            "Cups (US)": 0.2365882365,
            "Fluid Ounces (US)": 0.0295735296,
            "Tablespoons (US)": 0.0147867648,
            "Teaspoons (US)": 0.0049289216
        }

    # SPEED
    elif category == "Speed":

        units = {
            "Meters per Second": 1,
            "Kilometers per Hour": 0.2777777778,
            "Miles per Hour": 0.44704,
            "Feet per Second": 0.3048,
            "Knots": 0.514444
        }

    # DATA STORAGE
    elif category == "Data Storage":

        units = {
            "Bytes": 1,
            "Kilobytes (KB)": 1000,
            "Megabytes (MB)": 1000000,
            "Gigabytes (GB)": 1000000000,
            "Terabytes (TB)": 1000000000000,
            "Kibibytes (KiB)": 1024,
            "Mebibytes (MiB)": 1048576,
            "Gibibytes (GiB)": 1073741824
        }

    # TEMPERATURE
    if category == "Temperature":

        from_unit = st.selectbox(
            "Convert From",
            ["Celsius", "Fahrenheit", "Kelvin"]
        )

        to_unit = st.selectbox(
            "Convert To",
            ["Celsius", "Fahrenheit", "Kelvin"]
        )

        value = st.number_input(
            "Enter Temperature",
            value=0.0
        )

        def convert_temperature(value, source, target):

            if source == "Celsius":
                celsius = value

            elif source == "Fahrenheit":
                celsius = (value - 32) * 5 / 9

            else:
                celsius = value - 273.15

            if target == "Celsius":
                return celsius

            elif target == "Fahrenheit":
                return (celsius * 9 / 5) + 32

            else:
                return celsius + 273.15

        if st.button("Convert Temperature"):

            if (
                (from_unit == "Kelvin" and value < 0)
                or (from_unit == "Celsius" and value < -273.15)
                or (from_unit == "Fahrenheit" and value < -459.67)
            ):
                st.error("Temperature cannot be below absolute zero.")

            else:
                result = convert_temperature(
                    value,
                    from_unit,
                    to_unit
                )

                st.success(
                    f"{value} {from_unit} = "
                    f"{result:.4f} {to_unit}"
                )

    # OTHER CONVERSIONS
    else:

        value = st.number_input(
            "Enter Value",
            value=0.0
        )

        col1, col2 = st.columns(2)

        with col1:
            from_unit = st.selectbox(
                "Convert From",
                list(units.keys())
            )

        with col2:
            to_unit = st.selectbox(
                "Convert To",
                list(units.keys())
            )

        if st.button("Convert"):

            result = (
                value * units[from_unit] / units[to_unit]
            )

            st.success(
                f"{value:,.6f} {from_unit} = "
                f"{result:,.6f} {to_unit}"
            )

# =====================================
# ABOUT
# =====================================

elif menu == "About":

    st.subheader("👨‍💻 About This Application")

    st.write("### Student Information")

    st.write("Name: Gerald Brandon A. Seriño")

    st.write("Section: ME-2B")

    st.write("Project: Building and Deploying a Streamlit Web Application")

    st.write("Framework: Streamlit")

    st.write("Programming Language: Python")

    st.divider()

    st.write("### Purpose")

    st.write("""
    This application was created as part of an
    educational activity to demonstrate how to
    build and deploy an interactive web application
    using Python and Streamlit.
    """)

    st.success("Thank you for using my application!")

# =====================================
# FOOTER
# =====================================

st.divider()

st.caption(
    "© 2026 Student Productivity Dashboard | "
    "Created using Python and Streamlit"
)
