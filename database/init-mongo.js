// database/init-mongo.js
db.createUser(
    {
        user: "pdfuser",
        pwd: "pdfpassword",
        roles: [
            {
                role: "readWrite",
                db: "pdf_extractor"
            }
        ]
    }
)

db = new Mongo().getDB("pdf_extractor");

db.createCollection("extracted_data", { capped: false });