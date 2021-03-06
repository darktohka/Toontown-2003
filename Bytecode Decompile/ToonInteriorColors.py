from ToontownGlobals import *
wainscottingBase = [
 Vec4(0.8, 0.5, 0.3, 1.0), Vec4(0.699, 0.586, 0.473, 1.0), Vec4(0.473, 0.699, 0.488, 1.0)]
wallpaperBase = [
 Vec4(1.0, 1.0, 0.7, 1.0), Vec4(0.789, 1.0, 0.699, 1.0), Vec4(1.0, 0.82, 0.699, 1.0)]
doorBase = [
 Vec4(1.0, 1.0, 0.7, 1.0)]
floorBase = [
 Vec4(0.746, 1.0, 0.477, 1.0), Vec4(1.0, 0.684, 0.477, 1.0)]
baseScheme = {'TI_wainscotting': wainscottingBase, 'TI_wallpaper': wallpaperBase, 'TI_door': doorBase, 'TI_floor': floorBase}
colors = {DonaldsDock: {'TI_wainscotting': wainscottingBase, 'TI_wallpaper': wallpaperBase, 'TI_door': doorBase, 'TI_floor': floorBase}, ToontownCentral: {'TI_wainscotting': wainscottingBase, 'TI_wallpaper': wallpaperBase, 'TI_door': doorBase + [Vec4(0.8, 0.5, 0.3, 1.0)], 'TI_floor': floorBase}, TheBrrrgh: baseScheme, MinniesMelodyland: baseScheme, DaisyGardens: baseScheme, DonaldsDreamland: {'TI_wainscotting': wainscottingBase, 'TI_wallpaper': wallpaperBase, 'TI_door': doorBase, 'TI_floor': floorBase}, Tutorial: {'TI_wainscotting': wainscottingBase, 'TI_wallpaper': wallpaperBase, 'TI_door': doorBase + [Vec4(0.8, 0.5, 0.3, 1.0)], 'TI_floor': floorBase}, MyEstate: baseScheme}