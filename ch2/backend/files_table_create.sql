CREATE TABLE uploaded_files (
    id SERIAL PRIMARY KEY,
    filename TEXT NOT NULL,
    result_filename TEXT NOT NULL;
    type TEXT NOT NULL,
    date DATE NOT NULL,
    status TEXT NOT NULL
);
