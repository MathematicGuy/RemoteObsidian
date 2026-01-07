---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'



# Based on the mathematical formulations and architectural descriptions in the provided sources, specifically the "Hope Neural Learning Module" sections and the "Continuum Memory System" definitions, here is the feedforward workflow of the HOPE architecture drawn in text format.

### HOPE Architecture Feedforward Workflow

```text
+-----------------------------------------------------------------------+
|                       INPUT TOKEN (x_t) at time t                     |
+-----------------------------------------------------------------------+
                                   |
                                   v
+-----------------------------------------------------------------------+
|                   STEP 1: SELF-MODIFYING TITANS MODULE                |
|           (Replaces Standard Attention / Sequence Mixer)              |
+-----------------------------------------------------------------------+
|                                                                       |
|  [A] Adaptive Projections (Self-Referential Generation)    |
|      The model uses previous memory states to generate its own        |
|      parameters for the current step (Keys, Values, Rates).           |
|                                                                       |
|      k_t = M_k(x_t)      (Adaptive Key)                               |
|      v_t = M_v(x_t)      (Adaptive Value)                             |
|      η_t = M_η(x_t)      (Adaptive Learning Rate)                     |
|      α_t = M_α(x_t)      (Adaptive Decay/Retention)                   |
|      q_t = x_t * W_q     (Query is typically a standard projection)   |
|                                                                       |
|  [B] Memory Update (Inner Loop Optimization)                    |
|      The memory matrix (M) updates itself using the generated         |
|      parameters and a gradient-based rule (e.g., Delta Rule).         |
|                                                                       |
|      M_new = M_old - [Update based on k_t, v_t, η_t, α_t]             |
|                                                                       |
|  [C] Memory Retrieval (Forward Pass)                            |
|      The output (o_t) is retrieved from the updated memory using      |
|      the query.                                                       |
|                                                                       |
|      o_t = M_memory(q_t)                                              |
|                                                                       |
+-----------------------------------------------------------------------+
                                   |
                                   | o_t (Intermediate Output)
                                   v
+-----------------------------------------------------------------------+
|                  STEP 2: CONTINUUM MEMORY SYSTEM (CMS)                |
|           (Replaces Standard Static Feed-Forward/MLP Block)           |
+-----------------------------------------------------------------------+
|                                                                       |
|   The output passes through a chain of MLPs. Unlike static MLPs,      |
|   these update their weights at different "frequencies" (chunk sizes).|
|                                                       |
|                                                                       |
|   +--------------------------+                                        |
|   |  CMS Block 1 (High Freq) | <--- Updates every small chunk         |
|   |  Input: o_t              |      (Fast adaption)                   |
|   +--------------------------+                                        |
|                |                                                      |
|                v                                                      |
|   +--------------------------+                                        |
|   |  CMS Block 2 (Mid Freq)  | <--- Updates every medium chunk        |
|   |  Input: Output of B1     |                                        |
|   +--------------------------+                                        |
|                |                                                      |
|                v                                                      |
|              .....                                                    |
|                |                                                      |
|                v                                                      |
|   +--------------------------+                                        |
|   |  CMS Block K (Low Freq)  | <--- Updates rarely / Long-term        |
|   |  Input: Output of B(k-1) |      (Persistent knowledge)            |
|   +--------------------------+                                        |
|                                                                       |
+-----------------------------------------------------------------------+
                                   |
                                   v
+-----------------------------------------------------------------------+
|                        FINAL OUTPUT (y_t)                             |
+-----------------------------------------------------------------------+
```

### Explanation of Components

**1. Self-Modifying Titans (The "Head"):**
Unlike a standard Transformer where projections (Keys/Values) are fixed linear layers ($x \cdot W$), HOPE uses "Self-Modifying" memories. The model generates its own parameters ($k_t, v_t$) and optimization hyperparameters ($\eta_t, \alpha_t$) based on the input and the previous state of its parameter-generating memories. This allows the model to modify its own learning dynamics on the fly.

**2. Continuum Memory System (The "Body"):**
Instead of a static Feed-Forward Network (FFN/MLP) found in standard Transformers, HOPE uses a CMS.
*   **Structure:** It is a nested chain of MLPs: $y_t = MLP^{(f_k)}( \dots MLP^{(f_1)}(o_t) \dots )$.
*   **Function:** Each MLP in this chain updates its weights at a different frequency ($f$). High-frequency layers update often (learning immediate context), while low-frequency layers update rarely (preserving long-term knowledge), preventing catastrophic forgetting.

Based on the mathematical formulations and architectural descriptions in the provided sources, specifically the "Hope Neural Learning Module" sections and the "Continuum Memory System" definitions, here is the feedforward workflow of the HOPE architecture drawn in text format.

### HOPE Architecture Feedforward Workflow

```text
+-----------------------------------------------------------------------+
|                       INPUT TOKEN (x_t) at time t                     |
+-----------------------------------------------------------------------+
                                   |
                                   v
+-----------------------------------------------------------------------+
|                   STEP 1: SELF-MODIFYING TITANS MODULE                |
|           (Replaces Standard Attention / Sequence Mixer)              |
+-----------------------------------------------------------------------+
|                                                                       |
|  [A] Adaptive Projections (Self-Referential Generation)    |
|      The model uses previous memory states to generate its own        |
|      parameters for the current step (Keys, Values, Rates).           |
|                                                                       |
|      k_t = M_k(x_t)      (Adaptive Key)                               |
|      v_t = M_v(x_t)      (Adaptive Value)                             |
|      η_t = M_η(x_t)      (Adaptive Learning Rate)                     |
|      α_t = M_α(x_t)      (Adaptive Decay/Retention)                   |
|      q_t = x_t * W_q     (Query is typically a standard projection)   |
|                                                                       |
|  [B] Memory Update (Inner Loop Optimization)                    |
|      The memory matrix (M) updates itself using the generated         |
|      parameters and a gradient-based rule (e.g., Delta Rule).         |
|                                                                       |
|      M_new = M_old - [Update based on k_t, v_t, η_t, α_t]             |
|                                                                       |
|  [C] Memory Retrieval (Forward Pass)                            |
|      The output (o_t) is retrieved from the updated memory using      |
|      the query.                                                       |
|                                                                       |
|      o_t = M_memory(q_t)                                              |
|                                                                       |
+-----------------------------------------------------------------------+
                                   |
                                   | o_t (Intermediate Output)
                                   v
+-----------------------------------------------------------------------+
|                  STEP 2: CONTINUUM MEMORY SYSTEM (CMS)                |
|           (Replaces Standard Static Feed-Forward/MLP Block)           |
+-----------------------------------------------------------------------+
|                                                                       |
|   The output passes through a chain of MLPs. Unlike static MLPs,      |
|   these update their weights at different "frequencies" (chunk sizes).|
|                                                       |
|                                                                       |
|   +--------------------------+                                        |
|   |  CMS Block 1 (High Freq) | <--- Updates every small chunk         |
|   |  Input: o_t              |      (Fast adaption)                   |
|   +--------------------------+                                        |
|                |                                                      |
|                v                                                      |
|   +--------------------------+                                        |
|   |  CMS Block 2 (Mid Freq)  | <--- Updates every medium chunk        |
|   |  Input: Output of B1     |                                        |
|   +--------------------------+                                        |
|                |                                                      |
|                v                                                      |
|              .....                                                    |
|                |                                                      |
|                v                                                      |
|   +--------------------------+                                        |
|   |  CMS Block K (Low Freq)  | <--- Updates rarely / Long-term        |
|   |  Input: Output of B(k-1) |      (Persistent knowledge)            |
|   +--------------------------+                                        |
|                                                                       |
+-----------------------------------------------------------------------+
                                   |
                                   v
+-----------------------------------------------------------------------+
|                        FINAL OUTPUT (y_t)                             |
+-----------------------------------------------------------------------+
```

### Explanation of Components

**1. Self-Modifying Titans (The "Head"):**
Unlike a standard Transformer where projections (Keys/Values) are fixed linear layers ($x \cdot W$), HOPE uses "Self-Modifying" memories. The model generates its own parameters ($k_t, v_t$) and optimization hyperparameters ($\eta_t, \alpha_t$) based on the input and the previous state of its parameter-generating memories. This allows the model to modify its own learning dynamics on the fly.

**2. Continuum Memory System (The "Body"):**
Instead of a static Feed-Forward Network (FFN/MLP) found in standard Transformers, HOPE uses a CMS.
*   **Structure:** It is a nested chain of MLPs: $y_t = MLP^{(f_k)}( \dots MLP^{(f_1)}(o_t) \dots )$.
*   **Function:** Each MLP in this chain updates its weights at a different frequency ($f$). High-frequency layers update often (learning immediate context), while low-frequency layers update rarely (preserving long-term knowledge), preventing catastrophic forgetting.

# Excalidraw Data

## Text Elements
modern models often suffer from an "architecture illusion", whereas NL reveals that components like optimizers and attention mechanisms are actually associative memory modules that compress information at different frequencies. To exploit this insight, they develop the Continuum Memory System (CMS), which replaces traditional static memory with a more fluid, multi-level structure for better data retention. These concepts culminate in the Hope architecture, a self-modifying model designed to excel at continual learning and reasoning across exceptionally long contexts. Empirical tests demonstrate that Hope outperforms existing Transformers and recurrent models in maintaining knowledge over time and handling sequences of up to ten million tokens. Ultimately, the work suggests that increasing the "levels" of learning within an algorithm is the key to unlocking true self-improving artificial intelligence. ^yYVYhAQy

Based on the mathematical formulations and architectural descriptions in the provided sources, specifically the "Hope Neural Learning Module" sections and the "Continuum Memory System" definitions, here is the feedforward workflow of the HOPE architecture drawn in text format.

### HOPE Architecture Feedforward Workflow

```text
+-----------------------------------------------------------------------+
|                       INPUT TOKEN (x_t) at time t                     |
+-----------------------------------------------------------------------+
                                   |
                                   v
+-----------------------------------------------------------------------+
|                   STEP 1: SELF-MODIFYING TITANS MODULE                |
|           (Replaces Standard Attention / Sequence Mixer)              |
+-----------------------------------------------------------------------+
|                                                                       |
|  [A] Adaptive Projections (Self-Referential Generation)    |
|      The model uses previous memory states to generate its own        |
|      parameters for the current step (Keys, Values, Rates).           |
|                                                                       |
|      k_t = M_k(x_t)      (Adaptive Key)                               |
|      v_t = M_v(x_t)      (Adaptive Value)                             |
|      η_t = M_η(x_t)      (Adaptive Learning Rate)                     |
|      α_t = M_α(x_t)      (Adaptive Decay/Retention)                   |
|      q_t = x_t * W_q     (Query is typically a standard projection)   |
|                                                                       |
|  [B] Memory Update (Inner Loop Optimization)                    |
|      The memory matrix (M) updates itself using the generated         |
|      parameters and a gradient-based rule (e.g., Delta Rule).         |
|                                                                       |
|      M_new = M_old - [Update based on k_t, v_t, η_t, α_t]             |
|                                                                       |
|  [C] Memory Retrieval (Forward Pass)                            |
|      The output (o_t) is retrieved from the updated memory using      |
|      the query.                                                       |
|                                                                       |
|      o_t = M_memory(q_t)                                              |
|                                                                       |
+-----------------------------------------------------------------------+
                                   |
                                   | o_t (Intermediate Output)
                                   v
+-----------------------------------------------------------------------+
|                  STEP 2: CONTINUUM MEMORY SYSTEM (CMS)                |
|           (Replaces Standard Static Feed-Forward/MLP Block)           |
+-----------------------------------------------------------------------+
|                                                                       |
|   The output passes through a chain of MLPs. Unlike static MLPs,      |
|   these update their weights at different "frequencies" (chunk sizes).|
|                                                       |
|                                                                       |
|   +--------------------------+                                        |
|   |  CMS Block 1 (High Freq) | <--- Updates every small chunk         |
|   |  Input: o_t              |      (Fast adaption)                   |
|   +--------------------------+                                        |
|                |                                                      |
|                v                                                      |
|   +--------------------------+                                        |
|   |  CMS Block 2 (Mid Freq)  | <--- Updates every medium chunk        |
|   |  Input: Output of B1     |                                        |
|   +--------------------------+                                        |
|                |                                                      |
|                v                                                      |
|              .....                                                    |
|                |                                                      |
|                v                                                      |
|   +--------------------------+                                        |
|   |  CMS Block K (Low Freq)  | <--- Updates rarely / Long-term        |
|   |  Input: Output of B(k-1) |      (Persistent knowledge)            |
|   +--------------------------+                                        |
|                                                                       |
+-----------------------------------------------------------------------+
                                   |
                                   v
+-----------------------------------------------------------------------+
|                        FINAL OUTPUT (y_t)                             |
+-----------------------------------------------------------------------+
```

### Explanation of Components

**1. Self-Modifying Titans (The "Head"):**
Unlike a standard Transformer where projections (Keys/Values) are fixed linear layers ($x \cdot W$), HOPE uses "Self-Modifying" memories. The model generates its own parameters ($k_t, v_t$) and optimization hyperparameters ($\eta_t, \alpha_t$) based on the input and the previous state of its parameter-generating memories. This allows the model to modify its own learning dynamics on the fly.

**2. Continuum Memory System (The "Body"):**
Instead of a static Feed-Forward Network (FFN/MLP) found in standard Transformers, HOPE uses a CMS.
*   **Structure:** It is a nested chain of MLPs: $y_t = MLP^{(f_k)}( \dots MLP^{(f_1)}(o_t) \dots )$.
*   **Function:** Each MLP in this chain updates its weights at a different frequency ($f$). High-frequency layers update often (learning immediate context), while low-frequency layers update rarely (preserving long-term knowledge), preventing catastrophic forgetting. ^efnR45Ww

%%
## Drawing
```compressed-json
N4KAkARALgngDgUwgLgAQQQDwMYEMA2AlgCYBOuA7hADTgQBuCpAzoQPYB2KqATLZMzYBXUtiRoIACyhQ4zZAHoFAc0JRJQgEYA6bGwC2CgF7N6hbEcK4OCtptbErHALRY8RMpWdx8Q1TdIEfARcZgRmBShcZQUebQBGAE5tAAYaOiCEfQQOKGZuAG1wMFAwMogSbgg4ABY4ACtcHgAVACl0sshYRCrA7CiOZWCO8sxuZwA2JO0AZgB2AFYeOZ5E

tfXE/nKYcYAOCYXtCZq5lJTdrcgKEnVuRImUy6kEQmVpbh4zp+sh8VRH4oCKCkNgAawQAGE2Pg2KQqgBieIIJFIkaQTS4bCg5QgoQcYhQmFwiTA6zMOC4QK5NEQABmhHw+AAyrBhhJBB4acxgWCEAB1G6SbjxJ7ckHglkwNnoDmVJ64t4ccL5NAiwEQNgU7BqHaqr7qnHCOAASWIKtQBQAuk9aeRsqbuBwhIynoR8Vgqrh4jTcfilcxzaVOtB4H8

ZoCAL6ihAIYh3e4zfbxZNPRgsdhcNAzeITVNMVicABynDE3Gz8R4Mwm+xmruYABFMlBY9xaQQwk9NMJ8QBRYLZXLmoqdEqA8qVCQwACaADUp5IAIIARR2l3K3T+0CwUAgY4jgOt6qEcGIuGbcdVcwmcxvc12NQrNVr6qIHFBjud+CeMKxLbQbfwDt1UkUJmm3AAZN133/dsEGKKNiiDSAJ3Qac50XFcaQ3Kpm0wHcnjGNBnAWe5tESOYagmRNKyf

CjNnVXVUGcXYFkOY5TnOJ5rmIW40ESeJDiSXY5hmFJKOEhYnkkF43h3VVdgBYMfmlRTyjFXlCVhBEUWRJBO0xbFfQJaEtJJcgOHJSkcnw9V6UZSVpQgWU41FHlwQFHihVVVzxQQBzN2cn1hEVZVhSeTVMR1YV9WDQ1j1NIdD2DW1cHtC9UCdF11TdYgPQkJogrxYh/XNTKv3VMI/1QeIanImoahSHhhLzdNODLMSWoLDhiw4Uss2zKYFhqVi60bY

Jz1bWDO27Yg+yyazEqeY9Twmy9r1ve9H2fYMf3BdKAKA4NcLk9B9DYXLSA4VAztywDUDYWlmyu5ghFpWkmFQW0DFQaxUAAHQgSlsEkNQEH6EQEFQBlfC6gHqFQChpMCUJUELcDUECRh21QdQz1QPR9DgTgFtQIhwT+jhNSgQh9EIIx8x+/EfpkayM2usGQI4QhmH0ZgfsCH7wYIfAYB+gM2G1M9CEYdmztIUWbudcIcZAqB8YMOBAgDKGOFpWF9C

lzhmYpxw3qYazPsCABHIQcm1cJtFQZo2FQLAfDYNQVe5nXWFk+H1AQUXcsYGE4BVyGoVyN0hCEfRUAAWSyWFRaZGBuSyVAAAoIXjpkAEp4cR8xJApwIfExZXSUcanOAIVBuSl7BZeThG1EkH7rthSHaV8Eh4f0Z1qecYIQ/r4EhHBgW9dIVBNAQFmZ5W3AMfn1nOG0CnmmksJ1d6hA4DyfHnVpjgz0ht1w9QAAJTVIaBkHm0nhB4eXsJ8FpZwbsI

WkYDdZRO9uqgXKvslTEBxi7NwQRma72pk6AgFNgiUi5oMRmYDkaCGQf/TEIJtaQIPhmYWosYQoL0LkbczBHY9kJoQUg5g67Nm5HzXKZ0LKkmbCrPGN9EAU2ELIJg09eau0wNzWB/9mjmWYAIhm1g0FgxEFSNWN0gh8wvgbN0UQ3R/1QKCSmFBgjEGUJDNgaYcY0zvkzTmxBXzKApmEG2dtlYPVQMecBOMcjXWhmzKAvILKOwAKr4GpgbZsIt/bSQ

RrCUE9c/CGMYRwtWbpsDoK0QHf6EAR7KIBvdWkCCQiXS0dcdQF9foEGULCNucdvapPBKLbxziOC7RSaQW29cggfxpprYxWjKTU3pJLfAOsQlEEMXvbQPpKBgTwlUJRl0AHKOyU9aJZsZ5fTjr9AG99QZPyhoyIQsMaAIyRiEPmaMV5YzurjNWBMiZKkHKTQg4J7r4NpvTFgqDmZPRrldbIwNrDc0EVZQWUAhCELFoISW1MZbZDlgrc6Ss+aXPVoT

LWKjdb60NldPGpt3oKMtggexvVCAOydhAzA7tPZFNRb7aQYTA5AIQCHTUl9I6wJjnHROMLUCp3TnHbOucC6HOLivcuYgEXkGrgQgZDdqZN2hS3Qp7dl5y27r3Yg/dB6EGHgyqBYoJ7AqnrCWe89myLzPMvQInyMyOy3uESGpCxAHz5tgY+boz460vlwu+ogH5g31c/Dub8P5fx/lopRAzgGvFAa4yBAy8akNZXXRB+SUEyJXqETg3SklsFwTgfeX

zQXEP/vG8hlDqG0PcG4uJzDOBijdYiz190hB8NIAIvmWARFaPEWSKRbzU19HkRbMNqLrq4HUaOzB2jdH6MMfdExQTzFgMsdY1pBLRXZOcWHOpizaaMi8T4ihqAAlBLPqEy+FBInROULEw+iLEnJJQakgGGTAJZKcUmidCrimYvwGU2h6hKkIvCTU1xeJGkPuaZDQNzgOkgjMCm0gvTzBWAGeooIwyHFjJtJwKATI6Z/BzFh3IAAxVKDJGIXHVMdB

cwzMzoDEGQuELUZUEGo5G6ZJArF6XVPG8dTAHQSFqA0JobQaTlP8AQSZJ0IAzO+edeZD1FkvWWZbb66zAbeq2X6nZMMMxw0OebFGpzMYhAuarJFNySZkyMc8vDvamZnktUbH5nN/l80BZiYFoLQjgqsJCyGcr5YAPhfE8zKKdYCIxdA7F5tch4tXUSg9zshHkrVpSn2rwaXhyDtq0OzLsPR1jgnJOgXuXNl5TnfOhcQbA2FfgCuYrcAStrlKqIMr

m6BYVR3ZVn1VXqsCZq59Y9mnbOnkaheQCzUr0cxwa1287UljzU6l1p92EX1SQ2zZj8/Uv1ae/T+51v6/xQWG+lIDYzRtzbGq5+W4EDPfd0pm6CM0pqzTmh1+bGREM4EW7DJbUBULgDQuhAyGGH2raw8g7D6230bc21tQiO0oK7RZHtbnHtyNILiod7q1G5HHVonRbA9GxhncYj6873lLq0XY22e8+ZOJcVu9xO6iBG28eCXxh7+vBKCDAWlETSBR

Jele8IN6zN3uOSk8JT6cvMFfbSUmeSP1ty/T9H95T/1Q0A5DYDdTQMS1BE0lpUGYNdPg4h/pgy0OvAwzSXATa2AACVwh4e4OPZ+L43QICvjJd4qptA8EksBUCEEoKTUAh7naYe0BlXglsJCFR0oVESAADWcFbfAPB4jQeII77ARGhCJGaIYuYfisKhiqLaGMngqAEXGA1FIqR5gTE+AsCY1Yrw1CeIxZiJwEi7H2BMRIKRqxJBmNtco3FeKoDb9o

B8iRdiVgWApa8PAHxd+Ar7k68QjgkQfKJRIPAs9D/mN8QYKkfIaRMsSdA8IEApGzNmGkGIsRxXxJpG/0AJEUgUTSOyzJWQApoQ5QKo3J+RBRuAN9gx1IJRACqhAp5RgpJASowp1QIptRYBoong4oTQzRCgkpygUo0oPwspgwco8p0BcAJhCo/RQoY9PxowqoBI5hkxyJGoJ9IA0wuphR4g5hOoMweo+pqpdhsx7wh9VhRomwqoDpI9yguwio5oBw

8gSDypgxloz50peD1oh8UhWJao+DPc3wVDvwDdpCpp1QiZ1EhwxxhwRxVJOgUgxwCCyhbCHDtBF97hh8VgUgbxKwW81QRwwBHCRxnCwBXCygd8DhEh98UhD9j81hEw1wginC1xwiwAZhZh4hhJoiFhx8rxeDFgkjgjOhQi0iagEgagWIcxh8lgR8Zgg9AjiiyhSixwwAJgjhm9PgWDdgkgFgrxA8iiUibDWjkgKxV9hpywqjCjWimiwAWjAiKw59

hpWIfCBIph+IqJBiQjUjWiaoyIZhKIholh9hzgFgkgtiSidiFi5g59KxFgRCHwSI5hEgOCyhZj5iRws9tA+ij9Fg19qwxJx8KNGihiRw0ieB2iVizjhoaJWIZg+AZjQTOg0jRIjg1gH8aomp28cwDCQTtjhjAiDj3CTghoRCgSASrwLjmiriRwZhkhF8+jWJEgSIxD7wGi7CkSXDWinwyIKJlgsSFhdD4T2S3CPCVg7iap6oziejOSwjuT2jKI8j

287wxIITjgij3DVhxT5hJThosj4hZSyjdgyIlhKixJ+IH9PhgS7DNTyIj8dT6o9SZT8SwTWjciEgzg1gRJ7hKx7xXigjbTtSWDHTpSDSXTkS3TyirwxJ4gxIB9liagETGjAz7TgypT9TDS3TDgSIUh4h4SWJ0SzgRS3iUyJSQyMzwyuTAjWJvjh88ymoSJh8iykjIi988zYij9qj5hMzqyFShIl8V8Vh18Wzd9oj2y4iuy5geyRxZ959F96jBy18

aoRyoiYiJyT8pyQiDwnhNZlQIZFoKoaZnQz4AAFFFCGN3CDOPRCbKJPNgNgXQtgeOZoWo1oJkAAIUwDmBPKnCZGYBPNwHLx6AkCr1jHIFr3VEIiYmWGNKbJeOZOZOTGElzAYj2ErASH5OX3qN8Ioi4ggNVHIjnyHyfDOHOCrCyOtMgGkgyxOnKPIkXx8JbyeIH0DxFMBnPz+HsKcjAI/wRHv0f29H0lfyMl4rMjJB/2sj/2hn8ngOAJclAN8g8mn

ygLUjAJkvZDksKhCgDFQODHQKij1GwNxFwIPOSjtAQH4wygYOyndCgsBjmBoOKjoKstILUmr24CvF8PH2Gn4LalVCWF8u6gWw+HuHnxYICPHAbCkP2nMODHkN7H7AWmMKPBPA0OFE8qvBqKGnIm/GjxctUPKF2jMIjx3I9kHEKAJLsKpLmJpNFNWB0O8N8IfF2HojxMuMqs6AyNEMXymHvCfDpOElxI5MrLlMCJuMohEhIpauOAf2iOqo+M6D2Nj

NqmZOGhYjIqGocOnMWuSH4iaheIUiWBImLOSJGvBONM+DWGWEGlX2zBUq2rOu5LiDuoLN8JEJbxQraupI6rKFnKElYkrDzPqk2MRMerGsb1NLvBEgH0FJYk2reO2rKB6MyNiLb3b0Dw8JOveNqrKEPzIghJ6Pbz6MTPIhOucFbLHIP07NOEFM3PatdIWJ8PcKmCfGZPqKrCmCTJHGcC6ooohKyPqnHwXxvERrACQqOBOAeAH1iPql0KSJ5syJYt6

sFoGpFrBpHHbIDyonEgUkTOEn9IVu6v5r6qFsGtFrzONLb10MahZvhrAENr5uVv6uFrpu+oZo1soncMZKrETLOIrEorKAdqVoFudrNvVsWprIX0TIeGZJbwXw6laKDp6pDtNrVvpojIWOXznxEnH0mMGi5s6CTuNpVpdvNuvCODOArFRuTHqhEnlt5uDpNtVtdpqp+rFtOFSBarH2TAOJb3rsVuTqbtLvDoiJWG+LvHzL6JYKX0+u5obsHpLrDvT

qrI1pvG+Lb1yJbwxPYIDvtvnuLtDrTrdozo1oUlSGGmvBzGVKomZP7qNqdtTpboWoiMX2+IOIomomHx6IisLv3ofubvNpENmGOCfGGlqhYnqLvsdpToAZHrFv2COBEIhJ8IOKammMCOcDorvC6KYvooZIWEAZuLONWGhKhKuvlqwYYv6OYvwcAeNNQZppOBYKvAOAod5KodwbvFobgaSEbxEIKKvDpNqjpLYfopwcDzwdYvNrxtqgrHtPnJEJH1E

ewcYoka4akZ4ZeNmEurzNjOzD0N3swfYfEZoY0eXtGo1uiLIgUlWDAZODOANsoZMckdYmkcOAUjWBYghKGhWDrsTqcdUdMdcc0fGuItEjOHeoouUY4bUZYuCfMbSKSFCeiPCbIt6sMYCeoZcYIa3OXuqHPK1nwNFCPLq2bDPL3MCEvNtmvLKATxQgwFpA4Ed2Gj5AgqOgrxJG3BpCgsmDElmFyMDyP0Yt4Nau2HrzPpavuEakGrNLbzws8m4AOEb

yHy7o4ayKki3w+FIrP1+G4C4pgMhGv20l0lRCEsMhmlEvQFJAsgkupBtGkrgI0s5Ev3cnwtQHuu4t8nUplE0sQL8GQOcp/o1C1AMuqhinKBwISiKdsnMssrKldFss9F2EcpQPoNcoEHcrQATKyLOI4IYHzAzHSs2vxdaiCr3m4FYk3pIjxe5jGlXhipKvVHitmkSvKrRYKsgHUNWmqgypvC8NYpMN/AZcOnXC6YkHfNCHOzZ3CWCWkmCWB0+n1mP

K+TRzAU219REDrmASSUIHwRrR1gplSU6TMFyjAUEBEFFXhnJDBm/mBxFkvgBgbULAQE1YGXAiVy0XjjhWCABlsV9QzFVYdYgBZQK3ZWKxTjTjKyyVynpC5hVfhiOS13DgpneljGngoEpDAXPUFx7iJ3XXWwAHkTyex+ZgZNMIYgFwKro1ttxFXSBgkN4OAKZ4QW3r4i2S2FwNMtsK2iNq903M3UA+RIlc2KAKYKYAADSd46CmAAamcHnYXcXaXeX

ZXdXbXfXY3aXZnYpgAB9UB92D3D2j3j393jRCwTy/FmgnYC2ABpHsQsLOTAAAfSgDzmgQpzVhPa/aPZ3dnc3f/YA8A6A+cG3aum/fA4g8Pd/bA8g9g6/foD/eA6Q+Q6A9A73bg8PaZGaB7BPOqjQCZB7HAiI2cHjgLfrGNCIynDPYAHEnZjRmgFxCwmQE4yO/FwIS2MPoP0Pv3M5ncRVlYWQZEB2FwWYo4jYFAuV8VacxAE5CBMAmA33YPoO52UP

VO1OV20OMOtPtOdOf3d392CgFxLRUAFxTx8EZYzy2B6h/X9XM4mQ2lnBnccVWY65qOcgmAMVFP92uPj2bU5kBk9llZdyzBhA+YAtRZpVK4XYRkPPVtD4icYO9OOBuOD2f9UpV43lRtUlnVMcLZ04w5M4b3A5mB4YZwCBbYSvUBHcz5mA85HZwOfPdOmvmuGv9Oj3QQX3UAABeBOJ90ETOZ91949zOUz3AczyGIrmALzlr49xrw9+gTrnr+OJ9+gA

bl96b/dkbszvzVAMr3wBADbmb1AObg9wAduBFvevTu1uhuj2tuxudv3WkEtFqvmxDvOO2vD3ABG4Au+W8++u8O7u/G9QEbDwBgAUGd2mze8g5O/3atgu8G9QAACpB2n2rZbulxbZAsql4A7XRZX4BhTxSAwFOlrP+gMwvOYejuqftPGuCh3zjOOUW4/FUr2FM5jQOAlQZ5wJ7yw4C2bMjBPOmvKe/PwuR1gQ5Os54432uXlY1BA1nFWAH1wkYvId

zsv3Ke0vsgTVA3l4cRGsiVchnAMQwg0ElYs4EBtBlBtB4YxoogqulY6vv3KfqeXfoePuD3lulQKBuvevoQwFnALRmeVpIZjepWroOuoB4YFvI/UBzuY/vuoBjO3fkvXfU+4PaeIQGfw2qv55aEGU65M4iNYQM2ifUAAKAwoehf3f92/PeE4Am0s42B1uk2LU8/GAwFVlL4ZewFRe9ktEkuUv93Ul7F5Z6u0+Zvnfx+p/jvq/7ofun3wvM44ebvp+

IPJ/V/U/lP1Pt/t/QON/oP9+5+1Y2eGNshHA3UC2m16/X2KYN+EOOAVOd+n+kPNPtOsOcPeA0AIQC3Cxmgz2/E/E8cBOD2FI6O4pwXKX8thyAF8p84Wndfptz451Y10gnfEAO0E5tZe2sYZwEX1IAl9iACgeOOBFw7vldolfbzoh2f6UCAOr/Dfqvzm618r+DfCkAGEriSAFQiqfGCBAvhOJCBJ5A9H4gaQPJIMrWcwAnCIGVcB+B7AODvBl7hwa

ECMLfG5jVjRZcUAMKvPFnCBZJM4wMPEELjwy1dtA8A2gU71n7GDXec3R/upxnZmDyBKfbzvuwqyoASBBuaqFnCvgZZUARGa2G+z3YAAeBdoehZ7KxtUgWHmMLE4G6CTBdg47qew4DX80ATfT9tD2G4kZuQP0bbuT104WCn+1gmwUYJ/Y2D3u0Q2DvQEKHp8PulgtTrkLMFzd0Ojg5wViF4CS8SAng7wfYP8HztAhwfNtGmAVixhCAhWHQW+HV4fd

0O7PeIagEv6yAG+Tid8vEAKF5CKhOQwofkKg5lClOpg79qUPWFr9Nhx7bQAcIOE7Cohg/NfscNa7FDIO2w84Se2yE79qhxg2oQ4NzhODdoqAG9lnG57e8vB+KRTn4ICFB8auGMKyPawk7c9BgzgE1HHFuGjDYhEwqYdf3XTvlM4oIcmj4OG4nkCW6cWLITmJwGIDuyfbjpUNU4PDaBqwm4cn2JFUDqRy7PfnQNv6r97+VImkSyJA57CMORGM9guH

RgFtL2F7K9pnBgDN9zBFA1kWKLZEcBJ247MdhwBbbwh/sZKOrCtjZhOIoQhMYmIOBlGI9EeO+STnti9amwjsYiNQGSCzh+dHWIQYgADDzjIBtRFMAQVZgDQE8B2yOSRPrA+iIxzYqAEnjZwshZxJuEQPbhVzfaAp6Q8nK0YIKVCUhSYuAGAAzEzgAASTAP9D+jYBiAbANWHyATECor47bBXsrABj2d9RB2ENIMCyQBYEss2BABTBOwq8gRcve6BQ

Cuia8MufMRMRHyj4vtsx7yKmDTDpgYoKYkgUMKQBbHa8s4CYv6H9Hni4AX28MScQQDgAgQuxb7UPmAmlbnw4hDfVNEa0xjsA9ktiVrEYgVwNjRxTAZwHWNETtZKxTsEGG5kZBE5tc/ncBDWJLGiwGxCXRXE9xQTEAYAp8WmNgHpxXRUkPcGAI2wpjai4gqAENk6EKyM8SskbDOJnHNEQB3y50GANaNtGI8KY7PdOI1nXT49G4ng6vNgOL4DtnWUA

bNlEkL5EZCwBAogW+z1hFR3UDcVAUT03gSJUc8MXMcW3zFuYoJucRtsj33baiWQw2P1JhNQDGgEkfE/0OeE4Hjp10vA+QKgATFCi1YS3IgQAD1gAmcWkH1zzgRhM4Y7P6OmMPi8DtJukp9vEAMmZxEhb7ScaZL5h5wExgkg9tqILy9QvkEknsJiHbi8D3UaWX5BfBl4qJD4FARQdAlwAmxv4znWLOoOk6ixExtIbMY7HcFvBnA8Uu2EQljEMxZBC

mdxJnHuxliuY+gM/r5nmxkI8IAqIuMEFJhE4Mp1sBKTGLjFvJZB5AQIPa0zi7kwgpAODDYgaTfZIRTAOOLiOnQHd4YwXVmCQjNTqRFxog6eIYhkB/xMM6ocCpJiqASsTe90ICTKzPBytG4dcARMqwDbvJ1Wk8LVuEB1Z6s/Ra2cJMaxIDnZzWogcIFa0QDag+koKR9BACdYutyAbrD1iggNFKwskYQMnvq23HS5g2N2NlEVk5SlYsg0bBALGzUAB

sE2XoqpOElTbEB+2pfSiSO3zbhJuJJbM6VphrzVsgJtbCLFADAmyjW2RMkzl2w1YCxMB2M0iaXyHY5sYQo7JtpKKnbbhRR4olkTQKa5nt+R17O9g+3+7vszEOMZrlv0Flii6R0/A/oyIFkKyqBwsjDu/1w7xB8OhHYjqR3I6UcaOdHBjkxxY71g2OHHcoZcOG6ID6sXKZ0aXxE7TZUAEnezqukhjxw5OCnG2cyPVn3D2RFIm2eh0M7GdRuQPSzqT

xVZZwixH8JzjFmpiud3OkOTIQe2F4ys5MAXMIHzGC57iwu2fSLgimi4py3U74psSMNtmnjMuhqbLgOliz5d/RxXUruVxelVcaujvC4acODk09Z+EfH3st366DcAeEcnbpNzIFyzZ+0fAeStylm3dR50sSGEGIJEijbZcfGeVd2HnDcF5MsR7smn/gvcV5WQ2fgnxnl/ct588jITLBB6xjweq8MThwAnmVzThy/H3gj2R58hUe6PTHm+IRQ493A9r

AiaxOJ4gho5acmfrbJ7lwC2udPLPpykBGs92enPVANzyZR88gk/Yr5E/Ofm+cZW2fYJLQmTGZwpeG6boVDDyBtIFeUuSGBeLV4wiq5lIdLmONTS69xUBvKAEb0lam9apmcC3lbxt5BA7ejuB3mP1m5ByoFXc49p7wQDe8luT7P3kxED5BDZ4XC7adolnGoBo+8MOPvDAT5J9dhkCiRRsLsEFBM+sMluBDzb4F8cBeAsvt5mwVFDThDA6Ycfzskt9

c+RKdvipjjipJu+7WUWH3xQSSCj2w/H+aIokXkijFwSw9okJnmL9l+DiqfpEqiXpy1ZAcnIQyOVmZKklR/LOOzyhH9CL+jAm/ol3H5Mj0lNIzWbB21mf8oJP/P/oWAAFAD44IAgtmAIgHv9oBFWRJRAu7mHteO+8JAQJydlgJ0BoglmSRNwGZs6JxA0gQYv9kVKSR4ilJdEucWIjmBOclWOwI7hBSroPA8Qf4kEGPJpUogpSfDGiXSDIYsggOPIP

Ck0UlBQCGKYnLSSZTCUmgiAFnCGF6D6YBg5JYsMMUrKcF+7BZahxWGwj+JzHBoVEnmGZw0p7cH4VbHREdCA+CC4Ib0PrgGxGQEQ4YUCpiGSTNxUABIZ1yU4pDQgasRrPd3AXQLohIKwDqSP37LL05KS5JdcIiVLD7hYK6IXUJeFQqmhxCloQir+GoBkVXQoESEL6GOBBhGgHFWIq5Vwim0aABETMIVxzCFhNQ9lbv05V9L1ezKxlfu1ZVQLyRhwo

4WyoBW3DdVZq49gap7l3DNV/y7jtyshVvCPhmcL4a0N+HtCARQQvmO1N5xuyUFg0qEbirGEErFVxSpESiLRF4r+lmI9MNiLVijSScR8k4Qe1pXUCtVgKooWmsWWodsl4/FWdP3KU5rn+VSnTpyMLDcjJhfIy9lnDUk9LjF2a4tf+1A5SiZRcohUeXGVFGxVRGsDUXkC1E6jHYcckjq+M7Qmi/RSEyGT7kawYS7RHAB0UIKdFCdS+rontPpgFg+iw

ZE6gMQoGXm1d+Y3cH2WAlfB5Jmp8YpMSmLTEZjB22YriXmMC58xCxDnA0Ydj/jljis14kXlnNQC0LQp9OCudXLbEJiOxmi5cT2P56RYhxiAEcYwq17nrJx04jRfOPwCLiZxUAbsauLUWpI3QiIiGZDDzmhcx4bqJxCeNg0Zdzxpcy8RWOJRbxvYwsB8ZfBOx1Jg0b4+LhXKKn/wfxf48wIBMvggSaZEEx2NBJhlwSI2PKM0ZDNQk/jZ1WEjgDhOb

B4SnEBEjAcRJsVkT54lErOERhokzKGJM0ZiSMqdgcT3RLAO9TxIfUdwKsrk4SYj1El6oIYEkqSUm2XiyTzsuyxSeILQCqSfuWknSXpNBA2SUxjksQSeQsl6TrJhktxQ5IzFOSXJ4EtyYjw8lbrvJvkkLQFNvHyTgp3q8hXzDuWyQHly8FQRbFeXYBEpCY5KY7zhUNSpOWUs9a1OUX5SrohUgGf/BphlS3UxaKqVVgZCQwuZ1W1dNlJal8w2pIIxK

d1KYB9S6pEIoNYmvxECpJpUcaaVEFmnVY62i00RCtOSjYZcM9MYULPUgB6xiMpGEWNwEopbg8IrGZQLRnSRIybIwYNMMxnwCXbrt3iOADSB4xe5SAcLaynpVoTiZ8A608VqovXFi99pj2utgPFKYnSWFjM86eGkum0Jrpw6HcV0lNb1xhAz0yrta3em48g2P011igpa0JxvW1Yj5aDJjl4a0kwm2Cdn3hn6BEZyM+NqgETYYzu4fbNmVm2HZcyCZ

kMemSTIrZkyAplM9FNTLbV0y8xnbMtt22Zns6pl7MrnUThlFSjp2D/JtRkstWQdRZNa5oLe3vaPtm+eMD9pPNV1q7d+eatPgWqn5FrTdVQvVZh2w46y9ZRHEjmRwo5UdCwtHP/mbOY6GyrZ1K7VQgMGUOyUBhPMBC7LXhXR3ZNWveLJ3k6kAHF8sm3Uso12ZrbBocoziZyvmQwo5votscOoTkKJkMqANzpz0F6pLbZX6wBBZoI17J/FRGhhK4loU

5bGxpS8vacMA11tL4OXXFI3MK7NzdurcyrofIMEGKA9qetvce37lyKh5wo/pTvIm6Bx61Icq1fP1W4Xy59WegfftyX2j7j268uRZvNn0HtAeD3InYfJ31p7j2p8uRefKP2bd59wPMGLfIh4R6d9lPV+T13fko80e/SjHkwF/k4x/5XmIjcAu9GgLfRFPO3Sstp709zFgWVFXko54fRUFvPCDVgqr4V68FnKAhRL2IXS9stcvShYEv/ipJaFYCXFa

lzI3ML7MP6thdZE4VbTmkPCvhdb0f2BJl4wi4IJ3PoVj7x9vSqRU+y94zyFFAfAoAgcw1GwQNWi2Phor0XGLeD4+jPnAosUeL8+AyQvhzrsUV9V5Ti8JHXwb62Tm+3sVvp4vOyd9fFQQnvtn2IOyrThoS//eEsNVQGLVpw2JXIviV36yhfyi1Y2qT0adzdm/AI+YNyUn8Cl5/dhEqpKV380lfh6gc4ZqU8Av+9S//oAOAGgDwBTISASAKzjdL/dE

HAZfxz5gh60BIgpuBMrU1E8Zlrwg3BPMT2xHgOpavg1Bw+5rKmB3mVgdsuXjub9lfAw5Y6JOVNwzlthqQXNlIV1pqKM8PLdIAeVFbYsagxqXbASxaCvl9cfQXV28OPDnDUS21VYIzX2CIV1RxoTCrhXurEVMQkVaip6H/6MV4QlY8GvlWErclJK27qkPJUZDOAb+jVbsftVwCXDWna1cHJ2NVC9jeK+oW8J4DNCwEgqz1Z0MuOux0VZUqVZEJ4NM

r8V8I8NbMPmFrCfjwK5YTifT5/GMOAJikUauNVGLklChrw3buJM3CgTJIkE46sONRIXVbq6E+ca9VkLfVoIgNdNuGn3G0TCqyYRiZVWRrrJ0a4/bGtYDxrJ0ROMaU/LpMod6V9IlPanrqP1G6VQRl3pbrKUxH1T67Ro1p3LWVreRzQMWYKM8MT9dTep1di2snZi75RPYRUdYEiw9r1RtyftTzO1G6jh1L60scaIGBtjkJ06q0RABtFzqF1jyIBaH

qM3doTN66/DeAa3Vtid1e6kMVPCPX3IoxM8OrENvHHJjJxV6zMberbbmbNlT64sYaLfUfLqNiWTOYAl/XN6PxHe9sRouj7djU0vYl5JBuHHNmJxU4qIEhr+gLilx6GlccDp2kbjcNTMHcQynzn16jxze6uRRtL1UaP1NGjLfRooCPimNLsFjY2fY1E6uNpGACVhsxkiwBNiPSCdTrDZwyEJvKZCVJvQmhnMJ2E1hJaPwn17xlqmzQ+RM03UTaJvA

vTUxIvgsTozq6kzZV3pkWbl4Vm+LTZrs1PxHN0kjuK5rATdGFcSkrzWpIHm+bLJAWwyUFpi0hawtVkmyVFpMlEXnJ1mpHolrxDJbtR/2VLf5Nunex3NIU5vVMcPh4xCtTy3FCVrK0VbUpGWfrU1JzO5SGtj0AqRxqhilTCl7CTra+2621S+t/FurcNuUVcmxtWsCbVokLRDT62MpvEYYnm3GZFtRaGaTyDmlNwFpxqZaXbgdzO5WAu2mCIyyjxKg

fcNFYUAHjYogRmAkmSCEYRcthB4I4AJKIDDgBwB0BfwIMNADlabhhk7wLYAwCJQUAJWwlC5kcwkDwhaQuwWkIkDbAjAIA3e6yFJKyCiSr8RIY5jpEKvFXcgpV/QGlfOZFRLmX+cSlZDubFAir9cqAPVaIwPMpQQBZ5p1dqs9Wys5V15gsyxZJWRr9V8a35EeY/Mhr5QGa2VkdxIFUW1Uaa91fqt89IomBPUKpC6u5c6rZWIvkdp3TkYtrx10a1kD

Os4ZXcqoWekdYUT1XJMz2qoMEEeg1XtrY1qIAhk7YghPRjWZKstZ+tZAew+IAG0TmkjA38omOInN9euv1WobFAZoB03QBGREbL106+ZTWvSh4WnV5gFmkZAp5ooexA4HI2HzXhjiQ1JyMTfwBThoo1YXfMmBvBUReGzUTq0YHvL6BuACeegK3K8u5ldGdNBCKDaRurWZoG1iAJjaSs4gSAO2v4J8Dlu0JiALIfeBSxVskADRCACG7gE0D6Jw8IrC

APLeMiVW0ACeVCfgCTykBlAGITOJ8FrC8AUwzti4P8G+J5waQzuZQMeU/y237bWeN20fi7y8AJC7thYJ7ZqaQARrc19BQGxBsHbcbOQC6H/D5vqgcg+tw22gHdxPBsARAN7dnYgxPA/xfwHO2gSbQnqqmshSAAbEFxMBCw6XKu08FrvghSAetg21VHdxR2NQmgaOcwCZCnw4AOt9u1nZxhF3OrHmRec7GhBp32mwFGUJkC3Xva9k3ifQGjfnsE2d

ophYVtXbpAgh9ARY30Ubd3t1ZuQC4MnowGnv4AVC3dxwMwEzuHNKpUAROE6GPvgAxbdIHrYGH3ARggAA
```
%%