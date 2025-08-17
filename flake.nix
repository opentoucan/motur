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
            #pkgs.lib
            # Add any missing library needed
            # You can use the nix-index package to locate them, e.g. nix-locate -w --top-level --at-root /lib/libudev.so.1
          ];
          packages = builtins.attrValues {
            inherit
              (pkgs)
              uv
              ruff
              go-task
              pre-commit
              act
              google-chrome
              gcc
              glibc
                    zlib
              ;
          };
        };
      }
    );
  };
}
