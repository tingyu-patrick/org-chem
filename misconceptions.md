# Organic Chemistry：跨章節觀念迷思筆記（原本以為 vs 其實是）

> 讀書或寫題目時，遇到「原本以為是 A，但其實是 B」的觀念落差，直接加在下方表格。
> - `章節`：例如 `ch08`、`ch10`。
> - `關聯反應 (slug)`：可填單一反應（如 `oxymercuration`、`allylic-bromination`）、多個反應（以逗號分隔，如 `x2-addition, allylic-bromination`）或通則（如 `general`）。
> - `反應式`：採用**通式＋實例雙行格式**（第一行寫通式，第二行 `<br>` 寫課本具體例子）。
> - 在 `ch08/` 執行 `python build_index.py` 會自動讀取本檔案並更新 `ch08/index.md` 的統計數據。

| 章節 | 關聯反應 (slug) | 原本以為 | 其實是 | 關鍵原因 | 反應式 |
|---|---|---|---|---|---|
| `ch10` | `allylic-bromination` | NBS 自由基溴化時，radical 可能會生成在雙鍵碳 (vinylic C) 或其他一般烷基碳 (alkyl C) 上 | Radical 只會生成在 allylic position 上，不會生成在其他 carbon 上 | 1. **Resonance stabilization**：allylic radical 的未成對電子可與鄰近 $\pi$ 鍵共振分散（delocalized），穩定度遠高於一般 alkyl radical 與 vinylic radical。<br>2. **BDE 最低**：因為生成的 allylic radical 最穩定，allylic C–H 鍵的鍵解離能（bond dissociation energy, ~364 kJ/mol）為全分子最低（低於一般 alkyl C–H ~410 kJ/mol 與 vinylic C–H ~465 kJ/mol），因此 $\text{Br}\cdot$ 只會選擇性抓取 allylic H。<br>3. **NBS 的角色**：NBS 能維持極低濃度的 $\text{Br}_2$ 與 $\text{Br}\cdot$，避免發生 Ch08 的離子型雙鍵加成（`x2-addition`）。 `[needs-review]` | **通式**：$\text{C=C–CH}_2\text{–R} \xrightarrow[\text{CCl}_4]{\text{NBS, } h\nu} \text{C=C–CH(Br)–R}$<br>**實例**：$\text{Cyclohexene} \xrightarrow[\text{CCl}_4]{\text{NBS, } h\nu} \text{3-Bromocyclohexene (85\%)}$ `[needs-review]` |
| `ch10` | `alcohol-to-alkyl-halide` | 分子中若同時含有 ether、carbonyl 或 aromatic ring 等官能基，用 $\text{SOCl}_2$ 或 $\text{PBr}_3$ 轉化 $-\text{OH}$ 時其他官能基可能會受干擾或一起反應 | **Ethers、carbonyls 與 aromatic rings 通常不會干擾（don't usually interfere）**，$\text{SOCl}_2$ 與 $\text{PBr}_3$ 只會選擇性把 $-\text{OH}$ 轉成 $-\text{Cl}$ 或 $-\text{Br}$ | $\text{SOCl}_2$ 與 $\text{PBr}_3$ 反應條件溫和（如 $0\sim 35\,^\circ\text{C}$），不像濃 $\text{HX}$ 加熱會破壞酸敏感官能基（如裂解 ether），因此對其他官能基相容性極高且產率高。 | **通式**：$\text{R–OH} \xrightarrow{\text{SOCl}_2\text{ / py 或 PBr}_3\text{ / ether}} \text{R–Cl 或 R–Br}$<br>**實例**：$3\,\text{CH}_3\text{CH}_2\text{CH(OH)CH}_3 \xrightarrow[\text{Ether, } 35\,^\circ\text{C}]{\text{PBr}_3} 3\,\text{CH}_3\text{CH}_2\text{CH(Br)CH}_3\text{ (86\%)} + \text{H}_3\text{PO}_3$ |
| `ch10` | `alcohol-to-alkyl-halide` | 醇類轉鹵烷只討論轉成 $\text{R–Cl}$、$\text{R–Br}$、$\text{R–I}$（用 $\text{HCl}/\text{HBr}/\text{HI}$、$\text{SOCl}_2$、$\text{PBr}_3$），誤以為醇類無法直接轉成 alkyl fluorides ($\text{R–F}$) | **Alkyl fluorides ($\text{R–F}$) 也可以由醇類製備**，使用 **diethylaminosulfur trifluoride ($\text{[(CH}_3\text{CH}_2)_2\text{NSF}_3\text{]}$, DAST)** 或 **$\text{HF}$ / pyridine** | 課本明確指出可用替代氟化試劑將 $\text{R–OH}$ 轉為 $\text{R–F}$，在高產率下完成親核氟化取代。 | **通式**：$\text{R–OH} \xrightarrow{\text{[(CH}_3\text{CH}_2)_2\text{NSF}_3\text{] 或 HF / Pyridine}} \text{R–F}$<br>**實例**：$\text{Cyclohexanol} \xrightarrow[\text{Pyridine}]{\text{HF}} \text{Fluorocyclohexane (99\%)}$ |
<!-- 範例（填寫時請寫在註解外）：
| ch08 | oxymercuration | 產物會有立體選擇性 | 無法稱為 syn 或 anti | 第二步 NaBH4 還原會把立體化學洗掉 (scrambles stereo) | **通式**：$\text{Alkene} \xrightarrow[2.\text{ NaBH}_4]{1.\text{ Hg(OAc)}_2\text{, H}_2\text{O/THF}} \text{Markovnikov alcohol}$<br>**實例**：$\text{1-Methylcyclohexene} \xrightarrow[2.\text{ NaBH}_4]{1.\text{ Hg(OAc)}_2\text{/H}_2\text{O}} \text{1-Methylcyclohexanol}$ |
-->
