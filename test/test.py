# import numpy as np
# import matplotlib.cm as cm
# import matplotlib.pyplot as plt
# import matplotlib.cbook as cbook
# from matplotlib.path import Path
# from matplotlib.patches import PathPatch
#
# # 支持中文
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
# plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
#
# w, h = 512, 512
#
# with cbook.get_sample_data('ct.raw.gz', asfileobj=True) as datafile:
#     s = datafile.read()
# A = np.fromstring(s, np.uint16).astype(float).reshape((w, h))
# A /= A.max()
#
# fig, ax = plt.subplots()
# extent = (0, 25, 0, 25)
# im = ax.imshow(A, cmap=plt.cm.hot, origin='upper', extent=extent)
#
# markers = [(15.9, 14.5), (16.8, 15)]
# x, y = zip(*markers)
# ax.plot(x, y, 'o')
#
# ax.set_title('CT density')
#
# plt.show()


# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

# import matplotlib.pyplot as plt
# from matplotlib import cm
# from matplotlib.ticker import LinearLocator, FormatStrFormatter
# import numpy as np
#
#
# fig = plt.figure()
# ax = fig.gca(projection='3d')
#
# # Make data.
# X = np.arange(-5, 5, 0.25)
# Y = np.arange(-5, 5, 0.25)
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)
#
# # Plot the surface.
# surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
#                        linewidth=0, antialiased=False)
#
# # Customize the z axis.
# ax.set_zlim(-1.01, 1.01)
# ax.zaxis.set_major_locator(LinearLocator(10))
# ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
#
# # Add a color bar which maps values to colors.
# fig.colorbar(surf, shrink=0.5, aspect=5)
#
# plt.show()
#
# squares = []
#
# input_values = []
# for va in range(1, 13):
#     input_values.append(va)
#     squares.append(va ** 2)
# print(input_values)
# print(squares)
# plt.scatter(input_values, squares, c=squares, cmap=plt.cm.Blues,edgecolor='none', s=100)
# plt.title("苗心换2018话量数据", fontsize="24")
# plt.xlabel("月份", fontsize=15)
# plt.ylabel("话务量", fontsize=15)
# # plt.tick_params(axis='both', labelsize=14)
# # 保存图标信息
# plt.savefig('squares_plot.png', bbox_inches='tight')
# plt.show()


# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

# from matplotlib import cbook
# from matplotlib import cm
# from matplotlib.colors import LightSource
# import matplotlib.pyplot as plt
# import numpy as np
#
# # Load and format data
# filename = cbook.get_sample_data('jacksboro_fault_dem.npz', asfileobj=False)
# with np.load(filename) as dem:
#     z = dem['elevation']
#     nrows, ncols = z.shape
#     x = np.linspace(dem['xmin'], dem['xmax'], ncols)
#     y = np.linspace(dem['ymin'], dem['ymax'], nrows)
#     x, y = np.meshgrid(x, y)
#
# region = np.s_[5:50, 5:50]
# x, y, z = x[region], y[region], z[region]
#
# # Set up plot
# fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
#
# ls = LightSource(270, 45)
# # To use a custom hillshading mode, override the built-in shading and pass
# # in the rgb colors of the shaded surface calculated from "shade".
# rgb = ls.shade(z, cmap=cm.gist_earth, vert_exag=0.1, blend_mode='soft')
# surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, facecolors=rgb,
#                        linewidth=0, antialiased=False, shade=False)
#
# plt.show()

from selenium import webdriver

browce = webdriver.Chrome()
