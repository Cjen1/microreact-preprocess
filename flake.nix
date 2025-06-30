{
  description = "Basic flakes";

  inputs = { flake-utils.url = "github:numtide/flake-utils"; };

  outputs = { self, flake-utils, nixpkgs }:
    flake-utils.lib.eachDefaultSystem (system:
      let pkgs = nixpkgs.legacyPackages.${system};
      in {
        packages = { };
        devShell = pkgs.mkShell {
          inputsFrom = [ ];
          buildInputs = [ 
            pkgs.python3
          ];
        };
      });
}
