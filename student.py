def student_details(usn,name,division,age):
    result=(
        f"USN:{usn}\n"
        f"Name:{name}\n"
        f"Division:{division}\n"
        f"Age:{age}"
    )

if __name__ == "__main__":
    usn="01fe24bca314"
    name="shree"
    division="E"
    age=19
    print(student_details(usn,name,division,age))