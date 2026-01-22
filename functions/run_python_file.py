import os, subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_path = os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs
        if not valid_target_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if target_path[-3:] != ".py":
            return f'Error: "{file_path}" is not a Python file'
        command = ["python", target_path]
        if args:
            command.extend(args)
        completed_process = subprocess.run(command, cwd=working_dir_abs, capture_output=True, text=True, timeout=30)
        res = []
        if completed_process.returncode != 0:
            res.append(f"Process exited with code {completed_process.returncode}")
        if not completed_process.stdout and not completed_process.stderr:
            res.append("No output produced")
        else:
            if completed_process.stdout:
                res.append(f"STDOUT: {completed_process.stdout}")
            if completed_process.stderr:
                res.append(f"STDERR: {completed_process.stderr}")
        return "\n".join(res)
    except Exception as e:
        return f'Error: executing Python file: {e}'

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file at the given relative file_path, optionally with arguments, and returns its output",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to execute the Python code, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                ),
                description="Optional list of string arguments to pass to the Python script",
            ),
        },
        required=["file_path"],
    )
)
        