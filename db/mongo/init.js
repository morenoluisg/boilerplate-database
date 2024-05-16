db.createUser({
    user: "user",
    pwd: "password",
    roles: [ { role: "readWrite", db: "project_db" } ]
  });
  db.createCollection("sample_collection");
  