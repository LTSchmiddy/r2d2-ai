# set(TARGET_CORE "${TARGET_PREFIX}core")

# add_library(${TARGET_CORE} SHARED)
# configure_target_output(${TARGET_CORE})

target_sources(
    ${TARGET_CORE}
    PUBLIC
    core.h
    core.cpp
)