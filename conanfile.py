from conans import ConanFile, CMake, tools


class CowConan(ConanFile):
    name = "COW"
    version = "0.1.0"
    license = "MIT"
    url = "https://github.com/rikdev/cow"
    description = "Set of libraries implementing copy-on-write technique"
    topics = ("conan", "header-only", "copy-on-write")
    generators = "cmake"

    def source(self):
        git = tools.Git()
        git.clone("https://github.com/rikdev/cow.git", "master")

    def build(self):
        cmake = CMake(self)
        cmake.definitions["FETCH_DEPENDENCIES"] = "OFF"
        cmake.definitions["BUILD_TESTING"] = "OFF"
        cmake.definitions["ENABLE_TOOLING"] = "OFF"
        cmake.definitions["BUILD_EXAMPLES"] = "OFF"
        cmake.configure()
        cmake.install()

    def package(self):
        self.copy("*.h", dst="include", src="include")

    def package_id(self):
        self.info.header_only()
