import io
from contextlib import redirect_stdout
from dejan import generate_ascii_tree

def save_ascii_tree_to_file(filename="dirtree.txt"):
    # Create a StringIO object to capture the output
    with io.StringIO() as buf, redirect_stdout(buf):
        generate_ascii_tree()  # Generate the ASCII tree
        output = buf.getvalue()  # Get the output from the buffer
    
    # Write the captured output to the file with UTF-8 encoding
    with open(filename, "w", encoding="utf-8") as file:
        file.write(output)

# Generate the ASCII tree and save it to dirtree.txt
save_ascii_tree_to_file()
