from student import student_details

def test_student_details():
    expected_output=(
        "USN:01fe24bca314\n"
        "Name:shree\n"
        "Division:E\n"
        "Age:19"

    )
    assert student_details("01fe24bca314","shree","E",19)==expected_output
    