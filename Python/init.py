import os


class Init:
    def __init__(self, directory: str):
        self.directory = directory

    def initialize(self, cwd: str):
        """
        Actual reponse
        --------------
        hint: Using 'master' as the name for the initial branch. This default branch name
        hint: is subject to change. To configure the initial branch name to use in all
        hint: of your new repositories, which will suppress this warning, call:
        hint:
        hint:   git config --global init.defaultBranch <name>
        hint:
        hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
        hint: 'development'. The just-created branch can be renamed via this command:
        hint:
        hint:   git branch -m <name>
        Initialized empty Git repository in PATH/.git/
        """

        git_init_dir = os.path.join(cwd, ".git")
        os.mkdir(git_init_dir)

        files_list = ["HEAD", "config", "description"]
        folders_list = ["hooks", "info", "objects", "refs"]

        for folder in folders_list:
            os.mkdir(os.path.join(git_init_dir, folder))

        for file in files_list:
            filename = os.path.join(git_init_dir, file)
            with open(filename, "a"):
                os.utime(filename, None)

        return f"Initialized empty Git repository in {git_init_dir}/"

    def init(self):
        # If the repository has been initialized already
        cwd = os.path.join(os.getcwd(), self.directory)
        git_initialized = os.path.isdir(os.path.join(cwd, ".git"))

        if git_initialized:
            return f"Reinitialized existing Git repository in {cwd}/.git/"

        # If not, initialize.
        return self.initialize(cwd)
