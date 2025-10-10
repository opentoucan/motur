{
  description = "Motur flake";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };

  outputs = { nixpkgs, ... } @ inputs:
  let
      systems = [
        "aarch64-darwin"
        "x86_64-linux"
      ];
      forAllSystems = f:
        nixpkgs.lib.genAttrs systems (system:
          f {
            pkgs = import nixpkgs {
              inherit system;

              config.allowUnfree = true;
            };
          });
 in {
    devShells = forAllSystems (
      {pkgs}: {
        default = pkgs.mkShell {
          LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
            pkgs.stdenv.cc.cc
            pkgs.libGL
            pkgs.glib
          ];
          packages = builtins.attrValues {
            inherit
              (pkgs)
              uv
              ruff
              go-task
              pre-commit
              act
              chromium
              gcc
              glibc
              zlib
              mise
              renovate
              ;
          };
        };
      }
    );
  };
}
