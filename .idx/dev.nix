# To learn more about how to use Nix to configure your environment
# see: https://developers.google.com/idx/guides/customize-idx-env
{ pkgs, ... }: {
  # Which nixpkgs channel to use.
  channel = "stable-24.05"; # or "unstable"

  # Use https://search.nixos.org/packages to find packages
  home.packages = with pkgs; [
    # pkgs.go
    pkgs.sudo
    pkgs.python313Full
    pkgs.python313Packages.pip
    pkgs.pipenv
    pkgs.nodejs_20
    pkgs.nodePackages.nodemon
    pkgs.gh
    pkgs.git
    pkgs.curl
  ];

  # Sets environment variables in the workspace
  env = {};
  idx = {
    # Search for the extensions you want on https://open-vsx.org/ and use "publisher.id"
    extensions = [
      # "vscodevim.vim"
    ];

    # Enable previews

      previews = {
      enable = true;
      previews = {
        # Example: Run a web server for previewing web projects
        web = {
  command = ["python" "app.py" ];  # Example command to run for previews
          manager = "web";
          env = {
            PORT = "$PORT";  # Define environment variables for the preview
          };
        };
      };
    };

    # Workspace lifecycle hooks
    workspace = {
      # Runs when a workspace is first created
      onCreate = {
          # Example: install pip modules
        # pip-install = "pip install -r requirements.txt";
      };
      # Runs when the workspace is (re)started
      onStart = {
          # Example: start a background task to watch and rebuild  code
        # serve-streamlit = "python app.py";
      };
    };
  };
}
