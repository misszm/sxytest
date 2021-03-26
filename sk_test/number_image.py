# from matplotlib import pyplot as plt
# from matplotlib import image as img
# from PIL import Image, EpsImagePlugin
#
#
# def phone_num():
#     a_list = [[0, 9, 0, 9, 9, 9, 9, 0, 9, 9, 9, 9, 0, 9, 9, 9, 9, 0, 9, 9, 9, 9, 0, 9, 9, 9, 9, 0, 9, 9, 9, 9, 0, 9, 9, 9, 9, 0, 9, 9, 9, 9, 0, 9, 9, 9, 9, 0, 9, 9, 9, 9, 0],
#               [0, 9, 5, 1, 1, 2, 9, 3, 9, 1, 0, 9, 2, 1, 1, 2, 9, 3, 1, 1, 1, 9, 5, 1, 1, 1, 9, 5, 9, 1, 1, 9, 5, 9, 1, 0, 9, 2, 1, 1, 1, 9, 5, 1, 2, 0, 9, 1, 1, 1, 0, 9, 0],
#               [3, 9, 2, 1, 0, 9, 2, 2, 9, 1, 0, 9, 2, 1, 0, 1, 9, 2, 1, 2, 0, 9, 2, 1, 2, 0, 9, 2, 9, 9, 9, 9, 2, 9, 1, 0, 9, 2, 1, 2, 0, 9, 2, 0, 1, 2, 9, 2, 1, 2, 9, 3, 0],
#               [4, 9, 1, 2, 9, 1, 1, 0, 9, 1, 0, 9, 2, 2, 3, 9, 1, 0, 1, 0, 0, 9, 1, 1, 0, 0, 9, 1, 1, 2, 0, 9, 1, 9, 1, 0, 9, 2, 1, 0, 0, 9, 1, 3, 2, 9, 1, 0, 2, 9, 1, 0, 0],
#               [5, 9, 3, 2, 0, 9, 1, 0, 9, 1, 0, 9, 2, 0, 9, 2, 1, 0, 3, 0, 0, 9, 3, 3, 0, 0, 9, 3, 3, 0, 0, 9, 3, 9, 1, 0, 9, 2, 3, 0, 0, 9, 3, 1, 9, 0, 0, 3, 0, 2, 9, 1, 0],
#               [4, 9, 1, 1, 0, 2, 9, 0, 9, 1, 0, 9, 2, 9, 0, 2, 1, 0, 1, 0, 1, 9, 1, 1, 0, 1, 9, 1, 1, 0, 1, 9, 1, 9, 1, 0, 9, 2, 1, 0, 1, 9, 1, 9, 2, 1, 1, 0, 1, 2, 3, 9, 0],
#               [2, 9, 0, 9, 9, 9, 9, 0, 9, 9, 9, 9, 0, 9, 9, 9, 9, 0, 1, 0, 1, 9, 0, 1, 0, 1, 9, 0, 1, 0, 1, 9, 0, 9, 9, 9, 9, 2, 1, 0, 1, 9, 0, 9, 9, 9, 9, 1, 9, 9, 9, 9, 0]]
#     plt.matshow(a_list, cmap="bone", alpha=0.3, origin="upper")
#     plt.axis("off")
#     # plt.savefig("./图/phonenumber1111.gif", bbox_inches="tight", pad_inches=0, orientation="landscape", transparent=True)  # 横向, 透明
#     plt.savefig("./图/phonenumber.gif", bbox_inches="tight", pad_inches=0, orientation="landscape")  # 横向, 透明
#     plt.close()
#     plt.figure(figsize=(10, 1.5))
#     pic = img.imread("./图/phonenumber.gif")
#     plt.imshow(pic)
#     plt.axis("off")
#     # plt.savefig("./图/phonenumber_size.gif", bbox_inches="tight", pad_inches=0, orientation="landscape")  # 横向
#     plt.savefig("./图/phonenumber_size.gif", bbox_inches="tight", pad_inches=0, orientation="landscape", transparent=True)  # 透明
#     plt.close()
#
#
# def open_img():
#     EpsImagePlugin.gs_windows_binary = r'E:\gs9.53.3\bin\gswin64c.exe'
#     pic = Image.open("./图/ok.eps")
#     pic.save("./图/ok.jpg")
#
#
# if __name__ == '__main__':
#     open_img()