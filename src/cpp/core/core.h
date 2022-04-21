#pragma once

#define R2D2_EXPORT __declspec(dllexport) 
#define R2D2_C_EXPORT extern "C" R2D2_EXPORT 

R2D2_C_EXPORT void test_fn();