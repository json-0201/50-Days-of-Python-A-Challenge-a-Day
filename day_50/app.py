# website folder as a package
from website import create_app
app = create_app()

# if app.py is run
if __name__ == "__main__":
    app.run(debug=True)