# set(TARGET_RUNTIME "${TARGET_PREFIX}runtime")

# add_executable(${TARGET_RUNTIME})
# configure_target_output(${TARGET_RUNTIME})

# target_link_libraries(${TARGET_RUNTIME} ${TARGET_CORE})

target_sources(
    ${TARGET_RUNTIME}
    PUBLIC
    main.cpp
)