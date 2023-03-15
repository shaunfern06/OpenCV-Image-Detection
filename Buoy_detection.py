import cv2 as cv

a=0
img_colored = cv.imread('Photos/buoys.png')
img = cv.imread('Photos/buoys.png', 0)
templates = [cv.imread('Photos/green_buoy.png', 0), cv.imread('Photos/yellow_buoy.png', 0),
             cv.imread('Photos/red_buoy.png', 0)]

#   methods = [cv.TM_CCOEFF, cv.TM_CCOEFF_NORMED, cv.TM_CCORR, cv.TM_CCORR_NORMED, cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]
#   different template detection methods ^^^
for template in templates:
    img2 = img.copy()
    h, w = template.shape
    result = cv.matchTemplate(img2, template, cv.TM_CCOEFF_NORMED)  # out of all methods this had the best detection
    minval, maxval, minloc, maxloc = cv.minMaxLoc(result)
    location = maxloc  # in the case of ccoeff_normed this is the condition taken (for sqdiff and sqdiff_normed
    # location will be = minloc)
    bottom_right = (location[0] + w, location[1] + h)

    cv.rectangle(img_colored, location, bottom_right, (255, 255, 255), 1)  # outline
    rect_centre = (
    (location[0] + bottom_right[0]) // 2, (location[1] + bottom_right[1]) // 2)  # finding centre of buoys

    cv.circle(img_colored, rect_centre, 2, (255, 255, 255), thickness=2)  # circle at centre of buoys
    cv.line(img_colored, (img.shape[1] // 2, img.shape[0] // 2), rect_centre, (255, 255, 255),
            thickness=1)  # line from mid-point to centre of buoys

cv.circle(img_colored, (img.shape[1] // 2, img.shape[0] // 2), 2, (255, 255, 255),
          thickness=2)  # circle at mid-point of frame
cv.imshow('Final', img_colored)
cv.imshow('Original', cv.imread('Photos/buoys.png'))
cv.waitKey(0)
