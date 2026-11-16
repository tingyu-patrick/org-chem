# 有機化學期中模擬考卷（Chapters 7–10, 11-1 ~ 11-3）

> **考試範圍**：McMurry *Organic Chemistry*  
> - **Ch.07** Alkenes: Structure and Reactivity（不飽和度、烯類命名與 $E/Z$、烯類穩定度、親電加成、Markovnikov 規則、碳陽離子穩定度與重排、Hammond 假說）  
> - **Ch.08** Alkenes: Reactions and Synthesis（[試劑索引](ch08/index.md)｜[30 題練習](ch08/practice_30.md)）  
> - **Ch.09** Alkynes: An Introduction to Organic Synthesis（[試劑索引](ch09/index.md)｜[15 題練習](ch09/practice_15.md)）  
> - **Ch.10** Organohalides（[試劑索引](ch10/index.md)｜[15 題練習](ch10/practice_15.md)）  
> - **Ch.11 (11-1 ~ 11-3)** Nucleophilic Substitutions: Walden Inversion & The $\text{S}_\text{N}2$ Reaction（Walden 翻轉、$\text{S}_\text{N}2$ 二級動力學、背面攻擊與立體化學、受質／親核劑／離去基／溶劑效應）  
> - ⚙️ **機構總表**：[mechanisms.md](mechanisms.md) ｜ 📒 **迷思筆記**：[misconceptions.md](misconceptions.md)

---

## [1] 名詞解釋（Definitions & Key Terms，共 6 題，每題 3 分，共 18 分）

請簡要定義下列有機化學名詞，並各舉一例說明：

### - [ ] 1-1. Degree of Unsaturation（不飽和度 / 氫缺乏指數 IHD） *(Ch.07)*
### - [ ] 1-2. Markovnikov's Rule（馬可尼可夫規則，含現代電子解釋） *(Ch.07)*
### - [ ] 1-3. The Hammond Postulate（漢蒙假說） *(Ch.07 & Ch.10)*
### - [ ] 1-4. Regiospecific vs. Stereospecific Reaction（區域專一性 vs. 立體專一性反應） *(Ch.08)*
### - [ ] 1-5. Keto–Enol Tautomerism（酮—烯醇互變異構現象，並與 Resonance 區分） *(Ch.09)*
### - [ ] 1-6. Walden Inversion & Polar Aprotic Solvent（瓦爾登翻轉與極性非質子溶劑） *(Ch.11-1 ~ 11-3)*

<details>
<summary>💡 點擊展開 [1] 名詞解釋 標準答案與評分要點</summary>

1. **Degree of Unsaturation（不飽和度）**：
   - **定義**：分子相較於同碳數飽和無環烷烴（$\text{C}_n\text{H}_{2n+2}$）所缺少的氫分子對數（$\text{H}_2$ pairs）。每 1 個不飽和度代表分子中含有 **1 個環（ring）** 或 **1 個 $\pi$ 鍵**（雙鍵 $=1$，叁鍵 $=2$）。
   - **公式**：對於 $\text{C}_c\text{H}_h\text{N}_n\text{O}_o\text{X}_x$，$\text{Degree of Unsaturation} = c - \frac{h + x - n}{2} + 1$。
   - **舉例**：苯（$\text{C}_6\text{H}_6$）的不飽和度 $= 6 - 6/2 + 1 = 4$（1 個環 $+$ 3 個 $\pi$ 鍵）。

2. **Markovnikov's Rule（馬可尼可夫規則）**：
   - **定義**：
     - **經驗法則**：當不對稱試劑（如 $\text{HX}$）加成到不對稱烯類時，$\text{H}$ 會加在原本含較多氫（較少烷基取代）的雙鍵碳上，而鹵素 $\text{X}$ 則加在含較多烷基取代的雙鍵碳上。
     - **現代機構準則**：親電加成反應會優先透過**最穩定的碳陽離子中間體**（例如 $3^\circ > 2^\circ > 1^\circ$，或具共振穩定的 allylic/benzylic 碳陽離子）進行。
   - **舉例**：$\text{CH}_3\text{CH=CH}_2 + \text{HBr} \rightarrow \text{CH}_3\text{CH(Br)CH}_3$（經由 $2^\circ$ 碳陽離子，而非 $1^\circ$ 碳陽離子）。

3. **The Hammond Postulate（漢蒙假說）**：
   - **定義**：反應過渡狀態（Transition State, TS）的結構與能量，會較接近在能量上與它最相近的物種：
     - **吸熱步驟（Endergonic step，$\Delta G^\circ > 0$）**：過渡狀態能量接近產物（或中間體），故 TS 結構類似產物（**late transition state**），任何能穩定中間體的因素也會穩定 TS、降低活化能 $\Delta G^\ddagger$。
     - **放熱步驟（Exergonic step，$\Delta G^\circ < 0$）**：過渡狀態能量接近反應物，故 TS 結構類似反應物（**early transition state**）。
   - **舉例**：烯類加 $\text{HX}$ 形成碳陽離子為吸熱步驟，TS 結構類似碳陽離子，故較穩定的 $3^\circ$ 碳陽離子具有較低能量的 TS，生成速率最快；同理可解釋自由基溴化（吸熱，高選擇性）vs. 氯化（放熱，低選擇性）。

4. **Regiospecific vs. Stereospecific Reaction（區域專一性 vs. 立體專一性反應）**：
   - **Regiospecific（區域專一性）**：當不對稱試劑與不對稱受質反應時，在多個可能的位置異構物（constitutional isomers）中，僅生成（或高度優先生成）其中一種方向。例：`1-methylcyclohexene` 進行硼氫化氧化只生成 `2-methylcyclohexanol`。
   - **Stereospecific（立體專一性）**：起始物的立體化學構型直接決定產物的立體化學構型（不同立體異構物反應後得到不同的立體異構物產物）。例：*cis*-2-butene 與 $\text{Br}_2$ 行 *anti* 加成得 $(2R,3R)/(2S,3S)$ 外消旋體，而 *trans*-2-butene 與 $\text{Br}_2$ 反應則專一性地得到 *meso*-2,3-dibromobutane。

5. **Keto–Enol Tautomerism（酮—烯醇互變異構現象）**：
   - **定義**：由於質子（$\text{H}^+$）與 $\pi$ 鍵位置的快速重組，使乙烯醇（enol, $\text{C=C–OH}$）與羰基化合物（keto, $\text{CH–C=O}$）處於快速平衡的**結構異構物（constitutional isomers）**關係；由於 $\text{C=O}$ 鍵能較強，平衡通常極度偏向酮式（keto form）。
   - **與共振（Resonance）的差異**：互變異構物（Tautomers）有實際的**原子（$\text{H}$）位置移動**，屬於不同的分子（可分離或觀測）；共振結構（Resonance structures）僅有電子分佈改變、原子位置完全不動，代表同一個真實分子。

6. **Walden Inversion & Polar Aprotic Solvent（瓦爾登翻轉與極性非質子溶劑）**：
   - **Walden Inversion（瓦爾登翻轉）**：在 $\text{S}_\text{N}2$ 親核取代反應中，親核試劑從離去基的**正背面（$180^\circ$ back-side attack）**進攻對掌中心碳，導致該手性中心的絕對立體構型發生 $100\%$ 翻轉（如傘被風吹翻）。
   - **Polar Aprotic Solvent（極性非質子溶劑）**：具有大偶極矩（高介電常數 $\varepsilon$）但**不含 $\text{O–H}$ 或 $\text{N–H}$ 酸性氫**的溶劑（如 **DMSO、DMF、HMPA、$\text{CH}_3\text{CN}$、Acetone**）。它能有效溶合陽離子（如 $\text{Na}^+/\text{K}^+$），卻不會以氫鍵包圍陰離子親核劑，使「裸露（naked）」的親核劑維持極高能量與反應性，大幅加速 $\text{S}_\text{N}2$ 反應。
</details>

---

## [2] 說明題（Conceptual Explanations，共 6 題，每題 4 分，共 24 分）

### - [ ] 2-1. 【烯類穩定度與碳陽離子穩定度】 *(Ch.07)*
1. 將下列四個 $\text{C}_6\text{H}_{12}$ 異構物依**穩定度由高至低**排序，並排列其催化氫化熱（**$|\Delta H^\circ_{\text{hydrog}}|$ 放熱量絕對值由大到小**）：
   `1-hexene`、`cis-3-hexene`、`trans-3-hexene`、`2,3-dimethyl-2-butene`
2. 請以 **Hyperconjugation（超共軛效應）** 與 **Steric strain（立體張力）** 解釋上述穩定度順序；並說明為什麼碳陽離子穩定度亦遵循 $3^\circ > 2^\circ > 1^\circ > \text{methyl}$。

### - [ ] 2-2. 【自由基鹵化的選擇性與烯丙基位溴化】 *(Ch.10)*
1. 為什麼烷類進行自由基溴化（$\text{Br}_2, h\nu$）對 $3^\circ$ C–H 的選擇性（$1^\circ : 2^\circ : 3^\circ = 1 : 82 : 1640$）遠高於自由基氯化（$\text{Cl}_2, h\nu$，$1 : 3.8 : 5$）？請結合反應熱力學（$\Delta H^\circ$）與 **Hammond Postulate** 畫能量概念說明。
2. 當 `cyclohexene` 進行烯丙基位溴化（Allylic bromination）時，為何必須使用 **$\text{NBS}$（$N$-bromosuccinimide）/ $h\nu, \text{CCl}_4$** 而不能直接加入高濃度 $\text{Br}_2$？為何自由基只生成在 allylic C 上，而不生成在 vinylic C 或一般 alkyl C 上？

### - [ ] 2-3. 【炔類酸性與烷基化限制】 *(Ch.09 & Ch.11)*
1. 比較 **Ethane（$\text{CH}_3\text{CH}_3$）**、**Ethylene（$\text{H}_2\text{C=CH}_2$）** 與 **Acetylene（$\text{HC}\equiv\text{CH}$）** 的酸性強弱（標出約略 $\text{p}K_\text{a}$ 值），並以**碳原子混成軌域的 s-character（s 軌域成分比例）**解釋原因。
2. 乙炔負離子（$\text{R–C}\equiv\text{C:}^-\text{Na}^+$）與 `1-bromobutane` 反應可高產率得到烷基化產物，但若改與 `2-bromopropane` 或 `2-bromo-2-methylpropane` 反應卻幾乎得不到取代產物，主要產物反而變成什麼？為什麼？

### - [ ] 2-4. 【醇類轉化為鹵代烷的方法比較】 *(Ch.10 & Ch.11)*
1. 將 `(R)-2-butanol` 轉化為 `2-bromobutane` 時，若使用 **$\text{PBr}_3 / \text{ether}$** 與使用濃 **$\text{HBr}$**，在**反應機構、立體化學結果、以及是否容易發生碳陽離子重排**上有何差異？
2. 若分子中同時含有醚基（ether）或羰基（carbonyl）等官能基，為何實驗室偏好使用 $\text{SOCl}_2/\text{pyridine}$ 或 $\text{PBr}_3/\text{ether}$ 而非濃 $\text{HX}$？

### - [ ] 2-5. 【$\text{S}_\text{N}2$ 反應四大影響因素綜合判斷】 *(Ch.11-2 ~ 11-3)*
判斷下列各組反應中，**哪一個 $\text{S}_\text{N}2$ 反應速率較快**，並各用一句話說明關鍵原因：
- (a) `1-Bromopropane` vs. `1-Chloropropane`（與 $\text{NaCN}$ 反應）
- (b) `1-Bromo-2-methylpropane` vs. `1-Bromo-2,2-dimethylpropane`（與 $\text{NaI}$ 反應）
- (c) $\text{CH}_3\text{Br} + \text{NaOH}$ vs. $\text{CH}_3\text{Br} + \text{NaOCOCH}_3$
- (d) $\text{CH}_3\text{CH}_2\text{I} + \text{NaCN}$ 在 **$\text{CH}_3\text{OH}$（甲醇）** 中 vs. 在 **$\text{DMF}$（或 $\text{DMSO}$）** 中

### - [ ] 2-6. 【水合反應立體化學迷思：Oxymercuration vs. Hydroboration】 *(Ch.08)*
為何烯類的硼氫化氧化（`1. BH3, THF; 2. H2O2, OH-`）整體為嚴格的 **syn 加成**，而羥汞化還原（`1. Hg(OAc)2, H2O; 2. NaBH4`）雖然第一步經過三元環汞鎓離子（mercurinium ion）背面開環（*anti*），最終產物卻**不具立體專一性（scrambles stereochemistry）**？

<details>
<summary>💡 點擊展開 [2] 說明題 標準答案與評分要點</summary>

1. **2-1 烯類與碳陽離子穩定度**：
   - **穩定度由高至低**：`2,3-dimethyl-2-butene`（四取代）$>$ `trans-3-hexene`（反式二取代）$>$ `cis-3-hexene`（順式二取代）$>$ `1-hexene`（單取代）。
   - **氫化熱 $|\Delta H^\circ_{\text{hydrog}}|$ 絕對值由大到小**（越不穩定的烯類能量越高，氫化放熱越多）：`1-hexene` $>$ `cis-3-hexene` $>$ `trans-3-hexene` $>$ `2,3-dimethyl-2-butene`。
   - **原因**：
     1. **Hyperconjugation（超共軛）**：鄰近烷基上的 $\text{C–H}$ $\sigma$ 鍵軌域與雙鍵的空 $\pi^*$ 反鍵軌域部分重疊，加上 $sp^3$ 烷基碳與 $sp^2$ 雙鍵碳之間的鍵結更強，取代基越多越穩定。
     2. **Steric strain（立體張力）**：*cis* 異構物兩側大基團在雙鍵同側互相擠壓產生立體排斥，故 *trans* 比 *cis* 穩定。
     3. **碳陽離子穩定度**：帶正電的碳為 $sp^2$ 混成且具有空的 $p$ 軌域，周圍烷基越多，除了**誘導效應（Inductive effect）**推電子外，更有越多鄰近 $\text{C–H}$ $\sigma$ 鍵可與空 $p$ 軌域進行**超共軛（Hyperconjugation）**分散正電荷，故 $3^\circ > 2^\circ > 1^\circ > \text{methyl}$。

2. **2-2 自由基鹵化選擇性與 NBS 烯丙基位溴化**：
   - **(1) $\text{Br}\cdot$ vs. $\text{Cl}\cdot$**：在鏈傳播第一步（$\text{R–H} + \text{X}\cdot \rightarrow \text{R}\cdot + \text{H–X}$）中，氯化為**放熱反應（$\Delta H^\circ < 0$）**，依 Hammond 假說具有早期的過渡狀態（early TS），結構像反應物，C–H 鍵斷裂程度小，對自由基穩定度差異不敏感；而溴化為**吸熱反應（$\Delta H^\circ > 0$）**，具有晚期的過渡狀態（late TS），結構極像自由基中間體，因此 $3^\circ$ 自由基的穩定度優勢完全反映在過渡狀態活化能差上，選擇性極高。
   - **(2) NBS 角色與 Allylic 選擇性**（對應 [misconceptions.md](misconceptions.md)）：
     - 若直接加高濃度 $\text{Br}_2$，雙鍵會直接進行 Ch.08 的離子型親電加成生成 1,2-dibromocyclohexane；**NBS** 能維持極低濃度的 $\text{Br}_2$ 與 $\text{Br}\cdot$，抑制雙鍵加成並促成自由基取代。
     - **為何只在 allylic C**：Allylic radical 的未成對電子可與雙鍵 $\pi$ 電子**共振分散（resonance stabilization）**，使其穩定度遠高於一般 alkyl radical 與 vinylic radical，對應的 allylic C–H **鍵解離能（BDE $\approx 364\text{ kJ/mol}$）全分子最低**（低於 alkyl $\sim 410$ 與 vinylic $\sim 465\text{ kJ/mol}$）。

3. **2-3 炔類酸性與烷基化限制**：
   - **(1) 酸性排序**：**Acetylene**（$\text{p}K_\text{a} \approx 25$）$>$ **Ethylene**（$\text{p}K_\text{a} \approx 44$）$>$ **Ethane**（$\text{p}K_\text{a} \approx 60$）。
   - **解釋**：末端炔碳為 **$sp$ 混成（$50\%$ s-character）**，高於 $sp^2$（$33\%$）與 $sp^3$（$25\%$）。由於 $s$ 軌域比 $p$ 軌域更靠近帶正電的原子核，去質子化後形成的乙炔負離子（acetylide anion）孤對電子處於 $sp$ 軌域中，受到原子核更強的吸引而大幅穩定。
   - **(2) 烷基化限制**：乙炔負離子同時是強親核劑也是**強鹼**。只有對位阻小的**甲基或 $1^\circ$ 鹵代烷**才能順利進行 $\text{S}_\text{N}2$ 取代；若遇到位阻較大的 $2^\circ$（`2-bromopropane`）或 $3^\circ$（`2-bromo-2-methylpropane`）鹵代烷，$\text{S}_\text{N}2$ 背面攻擊受阻，會改行 **E2 脫去反應（Elimination）**，主要產物分別變成 **propene** 與 **2-methylpropene**（加上變回末端炔）。

4. **2-4 醇類轉鹵代烷（$\text{PBr}_3$ vs. $\text{HBr}$）**：
   - **(1)** `(R)-2-butanol` 與 **$\text{PBr}_3/\text{ether}$** 反應：先轉成 $-\text{OPBr}_2$ 離去基，再由 $\text{Br}^-$ 進行 **$\text{S}_\text{N}2$ 背面攻擊**，得到 $100\%$ 構型翻轉的 **(S)-2-bromobutane**，且**不會發生碳陽離子重排**。若用濃 **$\text{HBr}$** 加熱：$2^\circ$ 醇主要經由 **$\text{S}_\text{N}1$ 碳陽離子中間體**，立體化學發生外消旋化（racemization），且若鄰位有支鏈極易發生 1,2-hydride/alkyl shift 重排。
   - **(2)**（對應 [misconceptions.md](misconceptions.md)）$\text{SOCl}_2$ 與 $\text{PBr}_3$ 反應條件溫和（$0\sim 35\,^\circ\text{C}$，常加 pyridine 中和酸），**不會干擾分子中的 ether、carbonyl 或芳環**；而濃 $\text{HX}$ 強酸加熱會使醚鍵斷裂或引發副反應。

5. **2-5 $\text{S}_\text{N}2$ 反應速率比較**：
   - **(a) `1-Bromopropane` 較快**：$\text{Br}^-$ 的共軛酸 $\text{HBr}$ 酸性強於 $\text{HCl}$，故 $\text{Br}^-$ 為較佳的離去基（Leaving group：$\text{I}^- > \text{Br}^- > \text{Cl}^- \gg \text{F}^-$）。
   - **(b) `1-Bromo-2-methylpropane`（isobutyl bromide）較快**：後者 `1-bromo-2,2-dimethylpropane` 為 **neopentyl halide**，雖然形式上是 $1^\circ$，但 $\beta$-碳接了三個甲基，嚴重阻擋背面攻擊路徑，幾乎不發生 $\text{S}_\text{N}2$。
   - **(c) $\text{CH}_3\text{Br} + \text{NaOH}$ 較快**：同為氧原子親核劑時，鹼性越強親核性越強；$\text{HO}^-$ 無共振分散，親核性遠強於共振穩定的醋酸根 $\text{CH}_3\text{CO}_2^-$。
   - **(d) 在 $\text{DMF}$（或 $\text{DMSO}$）中較快**：$\text{DMF}$ 為**極性非質子溶劑（polar aprotic）**，不會以氫鍵束縛 $\text{CN}^-$；而 $\text{CH}_3\text{OH}$（極性質子溶劑）會透過氫鍵形成溶劑籠（solvent cage），大幅降低 $\text{CN}^-$ 的親核反應性。

6. **2-6 水合反應立體化學（Oxymercuration vs. Hydroboration）**：
   - **Hydroboration–oxidation**：第一步 $\text{B–H}$ 對雙鍵經由四元環過渡狀態進行**一步協同（concerted）的 *syn* 加成**，第二步 $\text{H}_2\text{O}_2/\text{OH}^-$ 氧化時，$-\text{OH}$ 以 **100% 構型保持（retention）**取代硼原子，故整體必為 *syn*。
   - **Oxymercuration–demercuration**：雖然第一步生成汞鎓離子並由 $\text{H}_2\text{O}$ 背面開環為 *anti*，但第二步使用 **$\text{NaBH}_4$ 還原脫汞**時，是經由**碳自由基中間體（radical mechanism）**將 $\text{C–HgOAc}$ 鍵還原為 $\text{C–H}$ 鍵，自由基可從平面兩側拿氫，因此把該碳的立體化學「洗掉」（non-stereospecific）。
</details>

---

## [3] Nomenclature（命名與結構互轉，共 10 小題，每題 2 分，共 20 分）

### Part A：請由結構寫出完整的 IUPAC 名稱（需標示 *cis/trans*、*E/Z* 或 *R/S* 立體化學）
- [ ] **3-1.** *(Ch.07)* 雙鍵碳 C2 接 $-\text{CH}_2\text{OH}$ 與 $-\text{CH}_3$；雙鍵碳 C3 接 $-\text{Br}$ 與 $-\text{CH(CH}_3)_2$，其中 $-\text{CH}_2\text{OH}$ 與 $-\text{Br}$ 在雙鍵**異側（opposite sides）**：
  $$\text{HOCH}_2\text{C(CH}_3)\text{=C(Br)CH(CH}_3)_2 \quad (\text{with } -\text{CH}_2\text{OH and } -\text{Br }\textit{trans}\text{ to each other})$$
- [ ] **3-2.** *(Ch.07)* 環己烯（cyclohexene）環上，雙鍵碳之相鄰位置有一個甲基，另一個雙鍵碳上有一個甲基，具體結構為：$\text{CH}_3\text{CH}_2\text{CH=C(CH}_3)\text{CH}_2\text{CH=CH}_2$（無環二烯）
- [ ] **3-3.** *(Ch.09)* $\text{H}_2\text{C=CHCH=CHC}\equiv\text{CH}$
- [ ] **3-4.** *(Ch.09)* $\text{CH}_3\text{CH}_2\text{CH(C}_2\text{H}_5)\text{C}\equiv\text{CCH(C}_2\text{H}_5)\text{CH(CH}_3)_2$
- [ ] **3-5.** *(Ch.10)* $\text{CH}_3\text{C(Br)(CH}_3)\text{CH}_2\text{CH(Cl)CH(CH}_3)_2$

### Part B：請由名稱畫出（或寫出示性式／立體描述）對應的化學結構
- [ ] **3-6.** *(Ch.07)* `(2Z,4E)-3-Chloro-2,4-hexadiene`
- [ ] **3-7.** *(Ch.07)* `1-Bromo-3-methylcyclohexene`
- [ ] **3-8.** *(Ch.09)* `3-Chloro-4,4-dimethyl-1-nonen-6-yne`
- [ ] **3-9.** *(Ch.10)* `(2R,3S)-2-Bromo-3-chlorobutane`
- [ ] **3-10.** *(Ch.10/11)* `Allyl iodide`、`Vinyl chloride` 與 `Benzyl bromide`（常見俗名轉結構）

<details>
<summary>💡 點擊展開 [3] Nomenclature 標準答案與解析</summary>

### Part A（結構 $\rightarrow$ 名稱）
- **3-1. `(E)-3-Bromo-2,4-dimethyl-2-penten-1-ol`**（若依純烯類與鹵素／羥基練習，不以醇為母體時：比較 C2 上的 $-\text{CH}_2\text{OH}$ [$\text{C–(O,H,H)}$] $>$ $-\text{CH}_3$ [$\text{C–(H,H,H)}$]；C3 上的 $-\text{Br}$ [原子序 35] $>$ $-\text{CH(CH}_3)_2$ [原子序 6]。因為兩端高優先序基團 $-\text{CH}_2\text{OH}$ 與 $-\text{Br}$ 在異側，必為 **(E)** 構型！）
- **3-2. `3-Methyl-1,4-heptadiene`**
  - **解析**：含兩個雙鍵的最長鏈為 7 碳（heptadiene）。從右端 $\text{=CH}_2$ 編號可得雙鍵位次 `(1,4)`，優於左端編號的 `(3,6)`，甲基位於 C3。
- **3-3. `1,3-Hexadien-5-yne`** *(Problem 9-26e)*
  - **解析**：兩端編號的多重鍵位次皆為 `(1,3,5)` 平手；依 IUPAC 規則，**平手時雙鍵（`-en-`）優先於叁鍵（`-yne`）拿較小數字**，故從左端雙鍵開始編號。
- **3-4. `3,6-Diethyl-2-methyl-4-octyne`** *(Problem 9-26f)*
  - **解析**：主鏈 8 碳，從左或從右算叁鍵都在 C4（`4-octyne` 平手）。此時比取代基位次：從右端（含異丙基端）編號得取代基位次 `(2,3,6)`，小於左端編號的 `(3,6,7)`！
- **3-5. `2-Bromo-4-chloro-2,5-dimethylhexane`** *(Problem 10-22c)*
  - **解析**：鹵素與烷基編號優先權相等，從左端編號得取代基位次 `(2,2,4,5)`，小於從右端的 `(2,3,5,5)`；寫名稱時按英文字母順序 `bromo` $\rightarrow$ `chloro` $\rightarrow$ `dimethyl`。

### Part B（名稱 $\rightarrow$ 結構）
- **3-6. `(2Z,4E)-3-Chloro-2,4-hexadiene`**：
  - 6 碳主鏈 $\text{C1–C2=C3(Cl)–C4=C5–C6}$。
  - **C2=C3 為 *Z***：C2 高優先為 $-\text{CH}_3$，C3 高優先為 $-\text{Cl}$（原子序 $17 > 6$），故 C2 的 $-\text{CH}_3$ 與 C3 的 $-\text{Cl}$ 畫在雙鍵**同側**。
  - **C4=C5 為 *E***：C4 高優先為 $-\text{C(Cl)=CHCH}_3$，C5 高優先為 $-\text{CH}_3$，故兩者畫在雙鍵**異側**（反式）。
- **3-7. `1-Bromo-3-methylcyclohexene`**：
  - 六元環內雙鍵為 C1=C2，為了讓雙鍵碳上的取代基拿最小數字，$-\text{Br}$ 接在 **C1**，順著雙鍵往 C2 走，C3 接 $-\text{CH}_3$。
- **3-8. `3-Chloro-4,4-dimethyl-1-nonen-6-yne`**：
  - $$\text{H}_2\text{C=CH}-\text{CH(Cl)}-\text{C(CH}_3)_2-\text{CH}_2-\text{C}\equiv\text{C}-\text{CH}_2\text{CH}_3$$
- **3-9. `(2R,3S)-2-Bromo-3-chlorobutane`**：
  - 當主鏈畫成鋸齒狀（C2–C3 單鍵為反式共平面）：C2 接 $-\text{Br}$、$-\text{H}$、$-\text{CH}_3$（優先序：$-\text{Br} > -\text{CH(Cl)CH}_3 > -\text{CH}_3 > -\text{H}$）；C3 接 $-\text{Cl}$、$-\text{H}$、$-\text{CH}_3$（優先序：$-\text{Cl} > -\text{CH(Br)CH}_3 > -\text{CH}_3 > -\text{H}$）。確認 C2 為順時針 $(R)$、C3 為逆時針 $(S)$。
- **3-10. 常見鹵代物俗名**：
  - **Allyl iodide（烯丙基碘）**：$\text{H}_2\text{C=CH}-\text{CH}_2\text{I}$（3-iodopropene）
  - **Vinyl chloride（氯乙烯）**：$\text{H}_2\text{C=CHCl}$（chloroethene）
  - **Benzyl bromide（苄基溴）**：$\text{C}_6\text{H}_5\text{CH}_2\text{Br}$（(bromomethyl)benzene）
</details>

---

## [4] 計算題（Quantitative & Analytical Problems，共 4 題，每題 4 分，共 16 分）

### - [ ] 4-1. 【不飽和度計算與臭氧化結構推導】 *(Ch.07 & Ch.08)*
某未知碳氫化合物 **A** 的分子式為 $\text{C}_{10}\text{H}_{16}$。
1. 計算化合物 **A** 的不飽和度（Degree of Unsaturation）。
2. 將 **A** 進行催化氫化（$\text{H}_2, \text{Pd/C}$），發現每 1 莫耳 **A** 最多只吸收 **1 莫耳 $\text{H}_2$** 得到分子式為 $\text{C}_{10}\text{H}_{18}$ 的產物 **B**。請問 **A** 含有幾個 $\pi$ 鍵與幾個環？
3. 若將某分子式為 $\text{C}_8\text{H}_{12}\text{ClNO}$ 的藥物分子進行結構分析，其不飽和度為多少？

### - [ ] 4-2. 【自由基溴化產物比例計算】 *(Ch.10)*
已知在特定溫度下，烷類進行自由基單溴化（$\text{Br}_2, h\nu$）時，不同級數氫原子的每個 H 相對反應速率為：
$$\text{Relative reactivity per H}: \quad 1^\circ : 2^\circ : 3^\circ = 1 : 82 : 1640$$
請列出算式並計算 **`2-methylbutane`（$(\text{CH}_3)_2\text{CHCH}_2\text{CH}_3$）** 進行自由基單溴化時，生成的 **4 種單溴代結構異構物**各自的理論相對百分比（%，取至小數點後一位）。

### - [ ] 4-3. 【$\text{S}_\text{N}2$ 反應動力學與旋光度計算】 *(Ch.11-1 ~ 11-2)*
將純的 `(S)-2-bromooctane`（已知純 $(S)$ 異構物的比旋光度 $[\alpha]_\text{D} = +36.0^\circ$）在 $\text{DMSO}$ 溶劑中與 $\text{NaOH}$ 進行親核取代反應，生成 `2-octanol`（已知純 `(R)-2-octanol` 的 $[\alpha]_\text{D} = -10.3^\circ$）：
$$\text{(S)-2-Bromooctane} + \text{NaOH} \xrightarrow{\text{DMSO}} \text{2-Octanol} + \text{NaBr}$$
1. 寫出此反應的速率定律式（Rate law）。若將 `[(S)-2-bromooctane]` 濃度變為原來的 **3 倍**，同時將 `[NaOH]` 濃度減半（變為 **0.5 倍**），反應初速率會變為原來的幾倍？
2. 若實驗改使用光學純度（enantiomeric excess, *ee*）為 **$80\%$ 的 `(S)-2-bromooctane`**（即含 $90\%$ $(S)$ 與 $10\%$ $(R)$），且完全依 $\text{S}_\text{N}2$ 機構反應完畢，請問所得 `2-octanol` 產物中 $(R)$ 與 $(S)$ 的百分比各為多少？產物的觀測比旋光度 $[\alpha]_\text{D}$ 為多少？

### - [ ] 4-4. 【有機氧化數／氧化態階層計算】 *(Ch.10-8)*
McMurry 課本（Section 10-8）定義有機反應中的氧化與還原：碳原子每增加一個 $\text{C–O / C–N / C–X}$ 鍵或減少一個 $\text{C–H}$ 鍵為氧化（Oxidation）；反之為還原（Reduction）。
1. 計算下列分子中標示碳原子的**形式氧化數（Oxidation state）**（規則：$\text{C–C}$ 計 $0$，$\text{C–H}$ 計 $-1$，$\text{C–O/N/X}$ 計 $+1$），並由**最還原態（最低氧化態）排到最氧化態（最高氧化態）**：
   (A) $\text{CH}_3\text{CH}_2\text{OH}$（C1） ｜ (B) $\text{CH}_3\text{CHO}$（C1） ｜ (C) $\text{CH}_3\text{CH=CH}_2$（C1 & C2 總和） vs. $\text{CH}_3\text{CH(OH)CH}_3$（C1 & C2 總和） ｜ (D) $\text{CH}_3\text{CO}_2\text{H}$（C1） ｜ (E) $\text{CH}_3\text{CH}_3$（C1）
2. 判斷下列三個轉換分別屬於 **Oxidation（氧化）**、**Reduction（還原）** 還是 **Neither（非氧化也非還原）**？
   - (i) $\text{CH}_3\text{CH=CH}_2 + \text{H}_2\text{O} \xrightarrow{\text{H}^+} \text{CH}_3\text{CH(OH)CH}_3$
   - (ii) $\text{CH}_3\text{C}\equiv\text{CH} \xrightarrow{\text{Li, NH}_3} \text{CH}_3\text{CH=CH}_2$
   - (iii) $\text{CH}_3\text{CH=CH}_2 \xrightarrow{\text{OsO}_4;\text{ NaHSO}_3} \text{CH}_3\text{CH(OH)CH}_2\text{OH}$

<details>
<summary>💡 點擊展開 [4] 計算題 標準答案與詳解</summary>

### 4-1 詳解：
1. **$\text{C}_{10}\text{H}_{16}$ 不飽和度**：$\text{IHD} = 10 - \frac{16}{2} + 1 = \mathbf{3}$。
2. **結構推導**：每莫耳 **A** 只吸收 1 莫耳 $\text{H}_2$，代表分子中只有 **1 個 $\pi$ 鍵（1 個雙鍵）**；剩餘的不飽和度 $3 - 1 = 2$ 代表含有 **2 個環（bicyclic alkene，雙環烯）**！
3. **$\text{C}_8\text{H}_{12}\text{ClNO}$ 不飽和度**：$\text{IHD} = 8 - \frac{12 + 1 - 1}{2} + 1 = 8 - 6 + 1 = \mathbf{3}$。

---

### 4-2 詳解（`2-methylbutane` 單溴化產率計算）：
分析 $(\text{CH}_3)_2\text{CH}-\text{CH}_2-\text{CH}_3$ 的 4 種不等價氫原子：
- **C1 & C1'（左側兩個對稱甲基，$1^\circ$ H 共 6 個）** $\rightarrow$ `1-bromo-2-methylbutane`：
  $$\text{相對量} = 6 \times 1 = 6$$
- **C2（中間次甲基，$3^\circ$ H 共 1 個）** $\rightarrow$ `2-bromo-2-methylbutane`：
  $$\text{相對量} = 1 \times 1640 = 1640$$
- **C3（亞甲基，$2^\circ$ H 共 2 個）** $\rightarrow$ `2-bromo-3-methylbutane`：
  $$\text{相對量} = 2 \times 82 = 164$$
- **C4（右端甲基，$1^\circ$ H 共 3 個）** $\rightarrow$ `1-bromo-3-methylbutane`：
  $$\text{相對量} = 3 \times 1 = 3$$
- **總和（Total）** $= 6 + 1640 + 164 + 3 = \mathbf{1813}$
- **各產物百分比**：
  1. `2-Bromo-2-methylbutane` ($3^\circ$)：$\frac{1640}{1813} \times 100\% = \mathbf{90.5\%}$
  2. `2-Bromo-3-methylbutane` ($2^\circ$)：$\frac{164}{1813} \times 100\% = \mathbf{9.0\%}$
  3. `1-Bromo-2-methylbutane` ($1^\circ$)：$\frac{6}{1813} \times 100\% = \mathbf{0.33\%}$ ($\approx 0.3\%$)
  4. `1-Bromo-3-methylbutane` ($1^\circ$)：$\frac{3}{1813} \times 100\% = \mathbf{0.17\%}$ ($\approx 0.2\%$)

---

### 4-3 詳解（$\text{S}_\text{N}2$ 動力學與旋光度）：
1. **速率定律式**：$\text{Rate} = k[\text{(S)-2-bromooctane}][\text{OH}^-]$（二級反應，對受質與親核試劑各為一級）。
   - 當 $[\text{RX}] \times 3$ 且 $[\text{OH}^-] \times 0.5$ 時，新速率 $\text{Rate}' = 3 \times 0.5\,\text{Rate} = \mathbf{1.5\text{ 倍}}$。
2. **立體化學與比旋光度計算**：
   - $\text{S}_\text{N}2$ 發生 $100\%$ 構型翻轉（Walden inversion）：原本的 $90\%$ $(S)$ 翻轉成 **$90\%$ `(R)-2-octanol`**，原本的 $10\%$ $(R)$ 翻轉成 **$10\%$ `(S)-2-octanol`**。
   - 產物的光學純度（*ee*）仍維持 $|90\% - 10\%| = \mathbf{80\%\text{ ee (R)}}$。
   - 產物觀測比旋光度 $[\alpha]_\text{D} = -10.3^\circ \times 80\% = \mathbf{-8.24^\circ}$。

---

### 4-4 詳解（有機氧化態計算）：
1. **C1 形式氧化數**：
   - (E) $\text{CH}_3-\mathbf{CH_3}$：$3\text{ 個 C–H} \rightarrow \mathbf{-3}$（最還原）
   - (A) $\text{CH}_3-\mathbf{CH_2OH}$：$2\text{ 個 C–H } (-2) + 1\text{ 個 C–O } (+1) \rightarrow \mathbf{-1}$
   - (B) $\text{CH}_3-\mathbf{CH=O}$：$1\text{ 個 C–H } (-1) + 2\text{ 個 C–O } (+2) \rightarrow \mathbf{+1}$
   - (D) $\text{CH}_3-\mathbf{CO_2H}$：$0\text{ 個 C–H } (0) + 3\text{ 個 C–O } (+3) \rightarrow \mathbf{+3}$（最氧化）
   - **排序**：**(E) $<$ (A) $<$ (B) $<$ (D)**。
2. **反應類型判斷**：
   - **(i) 烯類水合（$\text{Alkene} + \text{H}_2\text{O} \rightarrow \text{Alcohol}$）**：**Neither（非氧化也非還原）**！因為一個雙鍵碳多了 $\text{C–H}$（$-1$，還原），另一個雙鍵碳多了 $\text{C–O}$（$+1$，氧化），兩碳總氧化態淨變化為 $0$。
   - **(ii) 炔類還原為烯類**：**Reduction（還原）**（增加了兩個 $\text{C–H}$ 鍵）。
   - **(iii) 烯類雙羥基化（$\text{OsO}_4$）**：**Oxidation（氧化）**（增加了兩個 $\text{C–O}$ 鍵，無增加 $\text{C–H}$ 鍵）。
</details>

---

## [5] 反應機制（Reaction Mechanisms，共 4 題，每題 6 分，共 24 分）

請畫出完整步驟、所有反應中間體（含形式電荷與立體化學）、並以**彎箭頭（curved arrows）**清楚標示電子對（或單電子魚鉤箭頭）的流向：

### - [ ] 5-1. 【碳陽離子 1,2-Hydride Shift 重排機構】 *(Ch.07 & Ch.08)*
請畫出 **`3-methyl-1-butene`（$(\text{CH}_3)_2\text{CHCH=CH}_2$）** 與 **$\text{HBr}$** 反應時，同時生成一般加成產物 `2-bromo-3-methylbutane` 與重排主產物 **`2-bromo-2-methylbutane`** 的完整彎箭頭機構。

### - [ ] 5-2. 【環烯類加鹵醇（Halohydrin Formation）之立體與區域選擇性機構】 *(Ch.08)*
請畫出 **`1-methylcyclohexene`** 與 **$\text{Br}_2 / \text{H}_2\text{O}$** 反應生成 **`(1S,2S)/(1R,2R)`-*trans*-2-bromo-1-methylcyclohexanol** 的完整機構。需畫出橋環溴鎓離子（bromonium ion）中間體，並說明為何 $\text{H}_2\text{O}$ 選擇性進攻 C1 而非 C2。

### - [ ] 5-3. 【酸催化炔類水合與酮—烯醇互變異構機構】 *(Ch.09)*
請畫出 **`1-butyne`** 在 **$\text{H}_2\text{SO}_4, \text{H}_2\text{O}, \text{HgSO}_4$** 催化下水合生成 **`2-butanone`** 的反應機構（特別需完整畫出中間體 **Enol 經由酸催化互變異構化為 Ketone** 的兩個彎箭頭步驟）。

### - [ ] 5-4. 【醇與 $\text{PBr}_3$ 轉化為溴代烷之 $\text{S}_\text{N}2$ 機構】 *(Ch.10 & Ch.11)*
請畫出 **`(R)-2-octanol`** 與 **$\text{PBr}_3$（in ether）** 反應生成 **`(S)-2-bromooctane`** 的兩步彎箭頭機構，並畫出第二步 $\text{S}_\text{N}2$ 背面攻擊時的**五配位雙三角錐過渡狀態（Transition state $\ddagger$）**。

<details>
<summary>💡 點擊展開 [5] 反應機制 完整彎箭頭解析（附對應機構圖連結）</summary>

### 5-1. `3-Methyl-1-butene` + $\text{HBr}$ 重排機構（參見 [`mechanisms.md#1-hx-addition`](mechanisms.md#1-hx-addition)）
1. **Step 1（雙鍵質子化，Markovnikov 規則）**：
   - **彎箭頭 1**：$\text{C1=C2}$ 的 $\pi$ 鍵電子對攻擊 $\text{H–Br}$ 的 $\text{H}$。
   - **彎箭頭 2**：$\text{H–Br}$ 鍵電子對歸還給 $\text{Br}$，形成 $\text{Br}^-$ 與 **$2^\circ$ 碳陽離子中間體** $(\text{CH}_3)_2\text{CH}-\text{CH}^+-\text{CH}_3$。
2. **Step 2（1,2-Hydride Shift 氫負離子遷移）**：
   - **彎箭頭**：鄰位 C3 上的 $\text{C–H}$ $\sigma$ 鍵帶著一對電子（$\text{H:}^-$）直接遷移到相鄰 C2 的空 $p$ 軌域上，使 $2^\circ$ 碳陽離子轉化為能量更低、更穩定的 **$3^\circ$ 碳陽離子** $(\text{CH}_3)_2\text{C}^+-\text{CH}_2\text{CH}_3$。
3. **Step 3（親核捕獲）**：
   - **彎箭頭**：$\text{Br}^-$ 孤對電子攻擊 $3^\circ$ 碳陽離子（C3），生成主產物 **`2-bromo-2-methylbutane`**（部分未重排的 $2^\circ$ 碳陽離子被 $\text{Br}^-$ 捕獲則得次要產物 `2-bromo-3-methylbutane`）。

---

### 5-2. `1-Methylcyclohexene` + $\text{Br}_2/\text{H}_2\text{O}$ 鹵醇形成機構（參見 [`mechanisms.md#3-halohydrin`](mechanisms.md#3-halohydrin)）
1. **Step 1（形成三元環溴鎓離子 Bromonium ion）**：
   - **彎箭頭 1**：雙鍵 $\pi$ 電子攻擊 $\text{Br–Br}$ 的近端 $\text{Br}$。
   - **彎箭頭 2**：近端 $\text{Br}$ 的孤對電子回攻雙鍵碳，同步形成三元環。
   - **彎箭頭 3**：$\text{Br–Br}$ 鍵斷裂釋出 $\text{Br}^-$。此時假設 $\text{Br}^+$ 在環的背面（dash），則 C1 上的 $-\text{CH}_3$ 被推向正面（wedge）。
2. **Step 2（水分子背面區域選擇性開環）**：
   - **關鍵解釋**：在過渡狀態中，取代基較多的 **C1（$3^\circ$ 碳）能承載較多部分正電荷（$\delta^+$）**，電子供應穩定效果遠優於 C2（$2^\circ$ 碳）。
   - **彎箭頭 1**：溶劑 $\text{H}_2\text{O}$ 的氧孤對電子從三元環**正背面（wedge 側）**攻擊取代基較多的 **C1**，將 C1 的 $-\text{CH}_3$ 推回背面（dash）。
   - **彎箭頭 2**：$\text{C1–Br}^+$ 鍵斷裂，電子歸還給 C2 上的 $\text{Br}$（維持 dash）。
3. **Step 3（去質子化）**：
   - **彎箭頭**：另一分子 $\text{H}_2\text{O}$ 抓走 $-\text{OH}_2^+$ 上的質子，生成 **`trans-2-bromo-1-methylcyclohexanol`**（$-\text{OH}$ 與 $-\text{Br}$ 互為 *anti* 反式，故 $-\text{Br}$ 與 $-\text{CH}_3$ 在同側 *cis*！）。

---

### 5-3. `1-Butyne` 酸催化汞鹽水合與互變異構機構（參見 [ch09/cards/hgso4-hydration.md](ch09/cards/hgso4-hydration.md)）
1. **Step 1（形成乙烯基汞中間體與水攻擊）**：
   - 末端叁鍵 $\pi$ 電子攻擊親電性 $\text{Hg}^{2+}$，形成橋環／乙烯基陽離子中間體；$\text{H}_2\text{O}$ 攻擊取代基較多的內部碳 **C2**（Markovnikov），去質子化後得到有機汞烯醇，再經 $\text{H}_3\text{O}^+$ 質子化脫汞（protodemercuration）生成不穩定的內部烯醇 **`1-buten-2-ol`**（$\text{CH}_3\text{CH}_2\text{C(OH)=CH}_2$）。
2. **Step 2（酸催化 Keto–Enol Tautomerization：Enol 質子化）**：
   - **彎箭頭 1**：烯醇氧上的孤對電子向下推形成 $\text{C=O}$ 雙鍵。
   - **彎箭頭 2**：$\text{C=CH}_2$ 的 $\pi$ 鍵電子對攻擊酸 $\text{H}_3\text{O}^+$ 的 $\text{H}$，將質子加在末端 C1 上，形成質子化羰基中間體 $\text{CH}_3\text{CH}_2\text{C(=\!O}^+\text{H)CH}_3$。
3. **Step 3（去質子化得酮）**：
   - **彎箭頭**：$\text{H}_2\text{O}$ 孤對電子抓走 $=\!\text{O}^+\text{H}$ 上的質子，電子歸還給氧，得到穩定的 **`2-butanone`**（$\text{CH}_3\text{CH}_2\text{COCH}_3$）。

---

### 5-4. `(R)-2-Octanol` + $\text{PBr}_3$ 之 $\text{S}_\text{N}2$ 機構（參見 [`mechanisms.md#16c-pbr3`](mechanisms.md#16-alcohol-to-alkyl-halide)）
1. **Step 1（活化 $-\text{OH}$ 為優良離去基）**：
   - **彎箭頭 1**：`(R)-2-octanol` 的羥基氧孤對電子攻擊親電性的磷原子（$\text{Br–PBr}_2$）。
   - **彎箭頭 2**：一條 $\text{P–Br}$ 鍵斷裂，釋出 $\text{Br}^-$ 親核劑，形成質子化的二溴亞磷酸酯中間體 $\text{R–O}^+\text{(H)–PBr}_2$（此時 C2 碳氧鍵未斷，仍維持 $(R)$ 構型）。
2. **Step 2（$\text{S}_\text{N}2$ 背面攻擊與構型翻轉）**：
   - **彎箭頭 1**：剛離去的 $\text{Br}^-$ 從 C2 對掌中心的**正背面（$180^\circ$ back-side）**發動協同攻擊。
   - **過渡狀態 $\ddagger$**：C2 呈平面三角形 $sp^2$ 排列（$-\text{H}$、$-\text{CH}_3$、$-\text{C}_6\text{H}_{13}$ 在赤道平面），軸向兩端為部分鍵結的 $[\delta^-\text{Br}\cdots\text{C}\cdots\text{O(H)PBr}_2^{\delta^+}]^\ddagger$。
   - **彎箭頭 2**：$\text{C–O}$ 鍵同步斷裂，離去優良的中性離去基 $\text{HOPBr}_2$，得到 $100\%$ 構型翻轉的 **`(S)-2-bromooctane`**。
</details>

---

## [6] 合成題（Multistep Organic Synthesis，共 4 題，共 18 分）

請寫出由指定起始物合成目標產物的**每一步所需試劑**與**各步中間產物結構**：

### - [ ] 6-1. 【炔類碳鏈延長與立體專一性轉化為 *trans* 環氧烷】 *(Ch.08 & Ch.09，4 分)*
以 **Acetylene（$\text{HC}\equiv\text{CH}$）** 及不超過 3 個碳的鹵代烷為唯一碳源，合成 **`trans-2,3-epoxyhexane`**（即 $(2R,3R)/(2S,3S)$-2-ethyl-3-methyloxirane，反式雙取代環氧烷）。

### - [ ] 6-2. 【反馬可尼可夫水合 vs. 官能基位置移動】 *(Ch.08, Ch.10 & Ch.11，4 分)*
由 **`1-methylcyclohexene`** 出發，合成 **`trans-1-bromo-2-methylcyclohexane`**（注意：$-\text{Br}$ 在 C2，且與 C1 的 $-\text{CH}_3$ 互為 **trans**！請特別注意每一步的立體構型變化！）。

### - [ ] 6-3. 【烯丙基位溴化與 Gilman 偶合反應】 *(Ch.08 & Ch.10，5 分)*
由 **`cyclohexanol`（環己醇）** 與 **`bromoethane`（溴乙烷）** 為起始物，合成 **`3-ethylcyclohexene`**。

### - [ ] 6-4. 【跨章節綜合設計：末端烯轉化為少一碳的羧酸 vs. 多兩碳的末端醛】 *(Ch.08, Ch.09 & Ch.11，5 分)*
由 **`1-pentene`（$\text{CH}_3\text{CH}_2\text{CH}_2\text{CH=CH}_2$）** 出發，分別設計合成路徑製備下列兩個目標分子：
- **(a) `Butanoic acid`（$\text{CH}_3\text{CH}_2\text{CH}_2\text{CO}_2\text{H}$，4 碳羧酸）**
- **(b) `Heptanal`（$\text{CH}_3(\text{CH}_2)_5\text{CHO}$，7 碳末端醛，提示：可搭配 `HC≡CH` 延長碳鏈）**

<details>
<summary>💡 點擊展開 [6] 合成題 標準合成路徑與逆合成分析</summary>

### 6-1. Acetylene $\rightarrow$ `trans-2,3-epoxyhexane`
- **逆合成思考**：要得到 **trans-環氧烷**，必須由 **trans-2-hexene** 進行 `mCPBA` 環氧化（*syn* 協同加成保留 *trans* 構型）；而 `trans-2-hexene` 必由內部炔 **`2-hexyne`** 經由 **$\text{Li} / \text{NH}_3(\text{l})$ 溶解金屬還原**製備！
- **正向步驟**：
  1. $\text{HC}\equiv\text{CH} \xrightarrow[\text{2. CH}_3\text{Br}]{\text{1. NaNH}_2,\text{ NH}_3} \text{CH}_3\text{C}\equiv\text{CH}\text{ (Propyne)}$
  2. $\text{CH}_3\text{C}\equiv\text{CH} \xrightarrow[\text{2. CH}_3\text{CH}_2\text{CH}_2\text{Br}]{\text{1. NaNH}_2,\text{ NH}_3} \text{CH}_3\text{C}\equiv\text{CCH}_2\text{CH}_2\text{CH}_3\text{ (2-Hexyne)}$
  3. $\text{2-Hexyne} \xrightarrow{\text{Li, NH}_3(\text{l})} \textit{trans}\text{-2-Hexene}$（立體專一性 *anti* 還原）
  4. $\textit{trans}\text{-2-Hexene} \xrightarrow{\text{mCPBA, CH}_2\text{Cl}_2} \textbf{\textit{trans}-2,3-Epoxyhexane}$（外消旋混合物）

---

### 6-2. `1-Methylcyclohexene` $\rightarrow$ `trans-1-bromo-2-methylcyclohexane`
- **立體化學關鍵陷阱**！
  - 若直接用 `1-methylcyclohexene` 做硼氫化氧化（`1. BH3; 2. H2O2, OH-`），會得到 **`trans-2-methylcyclohexanol`**；若接著直接加 $\text{PBr}_3$，因為 $\text{PBr}_3$ 是 **$\text{S}_\text{N}2$ 構型翻轉**，會把 *trans* 翻轉成 **`cis-1-bromo-2-methylcyclohexane`**（錯誤立體異構物！）。
  - **正確解法（構型翻轉兩次，或先轉為 *cis*-醇 / *cis*-甲磺酸酯）**：
    - **路徑 A（經由 Tosylate 兩次 $\text{S}_\text{N}2$ 翻轉，或透過烯類轉換）**：
      1. `1-Methylcyclohexene` $\xrightarrow[\text{2. H}_2\text{O}_2,\text{ OH}^-]{\text{1. BH}_3,\text{ THF}}$ **`trans-2-methylcyclohexanol`**
      2. 若要將 *trans*-醇轉為 *trans*-溴代烷，必須經過**兩次 $\text{S}_\text{N}2$ 翻轉**：
         - Step 2a：`trans-2-methylcyclohexanol` $\xrightarrow{\text{TsCl, pyridine}}$ `trans-2-methylcyclohexyl tosylate`（構型保持）
         - Step 2b：$\xrightarrow{\text{CH}_3\text{CO}_2^-\text{Na}^+,\text{ DMF}}$ `cis-2-methylcyclohexyl acetate`（第一次 $\text{S}_\text{N}2$ 翻轉為 *cis*）$\xrightarrow{\text{OH}^-,\text{ H}_2\text{O}}$ `cis-2-methylcyclohexanol`
         - Step 2c：`cis-2-methylcyclohexanol` $\xrightarrow{\text{PBr}_3,\text{ ether}}$ **`trans-1-bromo-2-methylcyclohexane`**（第二次 $\text{S}_\text{N}2$ 翻轉回 **trans**！）

---

### 6-3. `Cyclohexanol` + `Bromoethane` $\rightarrow$ `3-Ethylcyclohexene`
- **逆合成思考**：目標分子在雙鍵的**烯丙基位（allylic position, C3）**多了一個乙基。只要先將 `cyclohexanol` 脫水成 `cyclohexene`，再用 **NBS** 在烯丙基位裝上 $-\text{Br}$ 得到 `3-bromocyclohexene`，最後與由 `bromoethane` 製備的 **Gilman 試劑 $\text{(CH}_3\text{CH}_2)_2\text{CuLi}$** 進行偶合即可！
- **正向步驟**：
  1. **製備烯丙基溴**：
     - $\text{Cyclohexanol} \xrightarrow{\text{POCl}_3,\text{ pyridine (or H}_2\text{SO}_4, \Delta\text{)}} \text{Cyclohexene}$
     - $\text{Cyclohexene} \xrightarrow{\text{NBS, } h\nu,\text{ CCl}_4} \text{3-Bromocyclohexene}$
  2. **製備二乙基銅鋰（Gilman reagent）**：
     - $\text{CH}_3\text{CH}_2\text{Br} \xrightarrow{\text{2 Li, pentane}} \text{CH}_3\text{CH}_2\text{Li} \xrightarrow{\text{0.5 CuI, ether}} (\text{CH}_3\text{CH}_2)_2\text{CuLi}$
  3. **Corey–House 偶合反應**：
     - $\text{3-Bromocyclohexene} + (\text{CH}_3\text{CH}_2)_2\text{CuLi} \xrightarrow{\text{ether}} \textbf{3-Ethylcyclohexene}$

---

### 6-4. `1-Pentene` $\rightarrow$ (a) `Butanoic acid` & (b) `Heptanal`
- **(a) `1-Pentene` $\rightarrow$ `Butanoic acid`（少 1 個碳的氧化斷裂）**：
  - 直接以酸性過錳酸鉀（或臭氧化）切斷末端雙鍵：
    $$\text{CH}_3\text{CH}_2\text{CH}_2\text{CH=CH}_2 \xrightarrow{\text{KMnO}_4,\text{ H}_3\text{O}^+} \textbf{CH}_3\textbf{CH}_2\textbf{CH}_2\textbf{CO}_2\textbf{H}\text{ (Butanoic acid)} + \text{CO}_2\uparrow$$
- **(b) `1-Pentene` $\rightarrow$ `Heptanal`（延長 2 個碳並轉為末端醛）**：
  1. **反馬可尼可夫水合 + 轉為 $1^\circ$ 溴代烷**：
     - $\text{1-Pentene} \xrightarrow[\text{2. H}_2\text{O}_2,\text{ OH}^-]{\text{1. BH}_3,\text{ THF}} \text{1-Pentanol}$
     - $\text{1-Pentanol} \xrightarrow{\text{PBr}_3,\text{ ether}} \text{1-Bromopentane}$（$1^\circ$ 鹵代烷，適合乙炔負離子 $\text{S}_\text{N}2$ 烷基化！）
  2. **乙炔負離子 $\text{S}_\text{N}2$ 烷基化延長 2 個碳**：
     - $\text{HC}\equiv\text{CH} \xrightarrow{\text{NaNH}_2,\text{ NH}_3} \text{HC}\equiv\text{C:}^-\text{Na}^+ \xrightarrow{\text{1-Bromopentane}} \text{CH}_3(\text{CH}_2)_4\text{C}\equiv\text{CH}\text{ (1-Heptyne)}$
  3. **末端炔硼氫化氧化得末端醛**：
     - $\text{1-Heptyne} \xrightarrow[\text{2. H}_2\text{O}_2,\text{ OH}^-]{\text{1. R}_2\text{BH (or BH}_3\text{, THF)}} \textbf{CH}_3(\textbf{CH}_2)_5\textbf{CHO}\text{ (Heptanal)}$
</details>
