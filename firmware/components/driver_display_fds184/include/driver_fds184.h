#ifndef NEW_ESP32_FIRMWARE_DRIVER_FDS184_H
#define NEW_ESP32_FIRMWARE_DRIVER_FDS184_H

#include <esp_err.h>
#include "compositor.h"
#include "color.h"

#define FDS184_WIDTH CONFIG_FDS184_WIDTH
#define FDS184_HEIGHT CONFIG_FDS184_HEIGHT
#define FDS184_BUFFER_SIZE FDS184_WIDTH*FDS184_HEIGHT*sizeof(Color)

esp_err_t driver_fds184_init(void);
void driver_fds184_set_brightness(int brightness_val);
void driver_fds184_set_framerate(int framerate_val);
void driver_fds184_switch_buffer(uint8_t* buffer);

Color* getFrameBuffer();

#endif //NEW_ESP32_FIRMWARE_DRIVER_FDS184_H
