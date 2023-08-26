from back import create_app
from back.database import db
from flask_migrate import Migrate

app = create_app()
migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(debug=True, port=8000, host="0.0.0.0")
