return {
  init_options = {
    compilationDatabaseDirectory = "build";
    index = {
      threads = 0;
    };
    clang = {
      extraArgs = { "-Iheaders" },
      excludeArgs = { "-frounding-math" },
    };
  }
}
