# Vectorized computation

## Numpy 中的向量化计算















## x86-64 SIMD

| 指令集   | 推出年份  | 寄存器宽度 | 寄存器数量 | 峰值吞吐增益（FP32） |
| -------- | --------- | ---------- | ---------- | -------------------- |
| MMX      | 1996      | 64-bit     | 8          | 2x (INT8)            |
| SSE      | 1999      | 128-bit    | 8          | 4x (FP32)            |
| AVX/AVX2 | 2011/2013 | 256-bit    | 16         | 8x (FP32)            |
| AVX-512  | 2016      | 512-bit    | 32         | 16x (FP32)           |
| AMX      | 2021      | 1024-bit   | 8 (TILE)   | 专用矩阵加速         |

**步骤**：

- **Load**：将数据从内存中加载到dst中。
- 计算：计算数据。
- **Store**：存储到内存中。

```c
#include <immintrin.h>			// 使用 SIMD 扩展

void add(uint32_t *A, uint32_t *B, uint32_t *C, uint32_t N) {
    for (int i = 0; i < N; i++) {
        C[i] = A[i] + B[i];
    }
}

void vectorAdd(uint32_t *A, uint32_t *B, uint32_t *C, uint32_t N) {
    size_t i = 0;
    size_t ii = 8;	// 256 / 32 = 8
    for (; i+ii <= N; i += ii) {
        __m256i va = _mm256_load_si256((__m256i *)(&A[i]);
        __m256i vb = _mm256_load_si256((__m256i *)(&B[i]);
        __m256i vc = _mm256_add_epi32(va, vb);
        _mm256_store_si256((__m256i *)(&C[i]), vc);
    }
}
```





























