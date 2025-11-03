import package
from package import module_a
from package import sub_package

print(package)
print(sub_package)
print(module_a)

#доступ к вложенным модулям и пакетам выполняется через точку

from package.sub_package import module_b
from package.module_a import NAME
from package.sub_package.module_b import NAME as NAME_B

print(module_b)
print(NAME)
print(NAME_B)