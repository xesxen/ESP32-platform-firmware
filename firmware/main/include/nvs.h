#include <sdkconfig.h>
#include <string.h>
#include <fcntl.h>
#include <nvs_flash.h>
#include <esp_log.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "esp_spi_flash.h"
#include "esp_system.h"

#include "system.h"

#ifndef NEW_ESP32_MAIN_NVS_H
#define NEW_ESP32_MAIN_NVS_H

esp_err_t nvs_format();
bool nvs_check_empty();
bool nvs_init();

#endif
