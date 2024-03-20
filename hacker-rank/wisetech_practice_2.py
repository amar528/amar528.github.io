class Folder:

    def __init__(self, max_capacity):
        self.readme = 0
        self.css = 0
        self.js = 0
        self.max_capacity = max_capacity
        self.capacity = 0

    def add_readme(self, css, js, readme):
        if self.readme == 1 or not self.has_capacity(css, js, readme):
            return False

        self.readme = 1
        self.capacity += 1
        return True

    def has_capacity(self, css, js, readme):
        if readme > 0 and self.readme == 1 and css + js <= readme:
            return False

        capacity_left = self.max_capacity - self.capacity

        if css == 0 and self.js > self.css:
            return False

        if js == 0 and self.css > self.js:
            return False

        return self.capacity < self.max_capacity

    def add_css(self, css, js, readme):
        if not self.has_capacity(css, js, readme):
            return False

        self.css += 1
        self.capacity += 1
        return True

    def add_js(self, css, js, readme):
        if not self.has_capacity(css, js, readme):
            return False

        self.js += 1
        self.capacity += 1
        return True

    def __str__(self):
        return (f'Folder readme: {self.readme} css: {self.css} js: {self.js} capacity: {self.capacity} '
                f'max_capacity: {self.max_capacity}')


def minFolders(css, js, readme, capacity):
    folders = []
    curr_folder = None

    while css > 0 or js > 0 or readme > 0:

        # print(f'readme: {readme} css: {css} js: {js}')

        if not curr_folder or not curr_folder.has_capacity(css, js, readme):
            curr_folder = Folder(capacity)
            folders.append(curr_folder)

        # readme
        while readme > 0 and curr_folder.add_readme(css, js, readme):
            readme -= 1

        # css
        while css > 0 and curr_folder.add_css(css, js, readme):
            css -= 1

        # js
        while js > 0 and curr_folder.add_js(css, js, readme):
            js -= 1

    # print('')
    # print(*folders, sep='\n')
    return len(folders)


if __name__ == '__main__':
    cssFiles = int(input())

    jsFiles = int(input())

    readMeFiles = int(input())

    capacity = int(input())

    result = minFolders(cssFiles, jsFiles, readMeFiles, capacity)

    print(result)
