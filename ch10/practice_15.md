# Ch10 Organohalides 精選 15 題練習清單（重質不重量・含命名與隱藏詳解）

> 對應課本檔案：[ch10.pdf](ch10.pdf)（McMurry *Organic Chemistry* Ch.10, pp. 307–308h）  
> 對應筆記索引：[index.md](index.md)

---

## 第一部分：IUPAC 命名與立體化學基礎（2 題）

### - [ ] 1. Problem 10-22 & 10-23 (p. 308c) ⭐⭐ 【鹵代烷 IUPAC 命名規則與陷阱】
**題目重點**：
1. **(10-22)** 為下列 5 個鹵代烷進行 IUPAC 命名：
   - (a) $\text{CH}_3\text{CH(CH}_3)\text{CH(Br)CH(Br)CH}_2\text{CH(CH}_3)_2$
   - (b) $\text{CH}_3\text{CH=CHCH}_2\text{CH(I)CH}_3$
   - (c) $\text{CH}_3\text{C(Br)(CH}_3)\text{CH}_2\text{CH(Cl)CH(CH}_3)_2$
   - (d) $\text{CH}_3\text{CH}_2\text{CH(CH}_2\text{Br)CH}_2\text{CH}_2\text{CH}_3$
   - (e) $\text{ClCH}_2\text{CH}_2\text{CH}_2\text{C}\equiv\text{CCH}_2\text{Br}$
2. **(10-23)** 畫出 `(c) 3-Iodo-2,2,4,4-tetramethylpentane` 與 `(d) cis-1-Bromo-2-ethylcyclopentane` 的結構。

<details>
<summary>💡 點擊展開答案與詳解</summary>

**鹵代烷 IUPAC 命名三大核心規則**：
1. **鹵素與烷基地位完全平等**：在編號優先權上，$-\text{F}, -\text{Cl}, -\text{Br}, -\text{I}$ 與 $-\text{CH}_3, -\text{CH}_2\text{CH}_3$ 一視同仁，皆視為一般取代基（双鍵／叁鍵則高於鹵素與烷基）。
2. **先比位次組合，平手再比英文字母**：從離第一個取代基較近的一端編號；若兩端得到的位次數字組合完全相同，則依英文字母順序（`bromo` < `chloro` < `ethyl` < `fluoro` < `iodo` < `methyl`）讓字母靠前的基團拿較小數字。
3. **最長主鏈優先**（若有雙鍵／叁鍵則優先選含多重鍵的最長鏈）。

- **10-22 詳解**：
  - **(a) 3,4-Dibromo-2,6-dimethylheptane**
    - **解析**：主鏈 7 碳（heptane）。從左端算取代基位次為 `(2,3,4,6)`；從右端算為 `(2,4,5,6)`。因為在第二個數字時 $3 < 4$，故從左端編號！
  - **(b) 5-Iodo-2-hexene**
    - **解析**：含雙鍵主鏈 6 碳，**雙鍵優先於鹵素**，故從左端編號使雙鍵在 C2。
  - **(c) 2-Bromo-4-chloro-2,5-dimethylhexane**
    - **解析**：主鏈 6 碳。從左端算取代基在 `(2,2,4,5)`；從右端算在 `(2,3,5,5)`。在第二個數字時 $2 < 3$，故從左端編號！
  - **(d) 3-(Bromomethyl)hexane**（或 **1-Bromo-2-ethylpentane**）
    - **解析**：若選最長碳鏈（6 碳 hexane），C3 上接一個複雜取代基 $-\text{CH}_2\text{Br}$（bromomethyl），命名為 `3-(bromomethyl)hexane`（McMurry 標準答案）；若以含溴碳鏈為主鏈則為 `1-bromo-2-ethylpentane`。
  - **(e) 1-Bromo-6-chloro-2-hexyne**
    - **解析**：含叁鍵主鏈 6 碳，從右端編號使叁鍵在 C2（`2-hexyne` 優於左起的 `4-hexyne`）。
- **10-23 結構要點**：
  - **(c)** 5 碳主鏈，C3 接 $-\text{I}$，C2 與 C4 各接兩個甲基：$(\text{CH}_3)_3\text{C}-\text{CH(I)}-\text{C(CH}_3)_3$。
  - **(d)** 五元環上 C1 的 $-\text{Br}$ 與 C2 的 $-\text{CH}_2\text{CH}_3$ 同為 wedge（或同為 dash）。
</details>

---

### - [ ] 2. Problem 10-16 (p. 308a) ⭐⭐ 【醇與 PBr3 反應的 3D 立體構型翻轉】
**題目重點**：圖中的溴代烷是由 `(S)-2-pentanol` 與 $\text{PBr}_3$ 反應製備而來（紅棕色球 $=\text{Br}$）。請為該產物命名、標示 $(R)$ 或 $(S)$ 構型，並說明此反應是構型保持（retention）還是構型翻轉（inversion）？

<details>
<summary>💡 點擊展開答案與詳解</summary>

- **答案**：產物為 **(R)-2-bromopentane**；反應發生了**構型翻轉（inversion of configuration）**。
- **解析**：
  1. 觀察 C2 對掌中心：最小基團 $-\text{H}$ 朝向後方（dash），朝向讀者的上方為 $-\text{Br}$（第 1 優先），右下方為丙基 $-\text{CH}_2\text{CH}_2\text{CH}_3$（第 2 優先），左下方為甲基 $-\text{CH}_3$（第 3 優先）。$1 \rightarrow 2 \rightarrow 3$ 為順時針方向，故為 **(R)-2-bromopentane**。
  2. **機構原因**：$\text{PBr}_3$（[`alcohol-pbr3`](cards/alcohol-pbr3.md)）先將 $-\text{OH}$ 轉為優良離去基 $-\text{OPBr}_2$，接著 $\text{Br}^-$ 從背面進行 **$\text{S}_\text{N}2$ 攻擊**，因此立體構型由原本的 $(S)$ 100% 翻轉為 $(R)$！
</details>

---

## 第二部分：自由基鹵化、旋光性與反應選擇性計算（3 題）

### - [ ] 3. Problem 10-24(a) & 10-48(a,b) (pp. 308c, 308h) ⭐⭐⭐ 【自由基氯化手性 vs. 自由基溴化產率計算】
**題目重點**：
1. **(10-24a)** 畫出並命名 `2-methylbutane` 進行自由基單氯化（monochlorination）可得的所有結構異構物，指出哪些產物具有手性（chiral）？是否有任何產物具有旋光性（optically active）？
2. **(10-48a,b)** 已知自由基溴化對 $1^\circ : 2^\circ : 3^\circ$ 氫的相對反應速率為 **$1 : 82 : 1640$**。計算 **(a) methylcyclobutane** 與 **(b) 3,3-dimethylpentane** 單溴化各產物的相對百分比（%）。

<details>
<summary>💡 點擊展開答案與詳解</summary>

1. **10-24(a) `2-methylbutane`（$(\text{CH}_3)_2\text{CHCH}_2\text{CH}_3$）單氯化**：
   - 共有 4 種不等價的氫，生成 **4 種結構異構物**：
     1. `1-chloro-2-methylbutane`（**具手性 chiral**，C2 為對掌中心！）
     2. `2-chloro-2-methylbutane`（無手性 achiral，C2 接兩個甲基）
     3. `2-chloro-3-methylbutane`（**具手性 chiral**，C2 為對掌中心！）
     4. `1-chloro-3-methylbutane`（無手性 achiral）
   - **旋光性判斷**：**沒有任何一個產物具有旋光性（None are optically active）**！因為起始物與試劑皆無手性（achiral），生成的掌性產物必為 **1:1 外消旋混合物（racemic mixture）**，旋光度為 0。

2. **10-48 相對百分比計算（公式：$\text{該位置 H 數量} \times \text{相對速率}$）**：
   - **(a) `methylcyclobutane`**：
     - 甲基上的 $1^\circ$ H（3 個）：$3 \times 1 = 3$
     - C1 上的 $3^\circ$ H（1 個）：$1 \times 1640 = 1640$
     - C2 & C4 上的 $2^\circ$ H（4 個）：$4 \times 82 = 328$
     - C3 上的 $2^\circ$ H（2 個）：$2 \times 82 = 164$
     - **總和** $= 3 + 1640 + 328 + 164 = 2135$
     - **各產物比例**：
       - `1-bromo-1-methylcyclobutane`：$1640 / 2135 = \mathbf{76.8\%}$
       - `1-bromo-2-methylcyclobutane`：$328 / 2135 = \mathbf{15.4\%}$
       - `1-bromo-3-methylcyclobutane`：$164 / 2135 = \mathbf{7.7\%}$
       - `(bromomethyl)cyclobutane`：$3 / 2135 = \mathbf{0.14\%}$
   - **(b) `3,3-dimethylpentane`（$\text{CH}_3\text{CH}_2\text{C(CH}_3)_2\text{CH}_2\text{CH}_3$）**：
     - C1 & C5 的 $1^\circ$ H（6 個）：$6 \times 1 = 6$
     - C3 上兩個甲基的 $1^\circ$ H（6 個）：$6 \times 1 = 6$
     - C2 & C4 的 $2^\circ$ H（4 個）：$4 \times 82 = 328$
     - **總和** $= 6 + 6 + 328 = 340$
     - **各產物比例**：
       - `2-bromo-3,3-dimethylpentane`：$328 / 340 = \mathbf{96.5\%}$
       - `1-bromo-3,3-dimethylpentane`：$6 / 340 = \mathbf{1.8\%}$
       - `3-(bromomethyl)-3-methylpentane`：$6 / 340 = \mathbf{1.8\%}$
</details>

---

### - [ ] 4. Problem 10-38 & 10-39 (p. 308f) ⭐⭐⭐⭐ 【自由基立體化學經典對決：外消旋化 vs. 非對映異構物】
**題目重點**：
1. **(10-38)** 光學活性的 `(S)-3-methylhexane` 經自由基溴化後，主要產物 `3-bromo-3-methylhexane` **完全不具旋光性**。該產物分子本身是否具手性（chiral）？由此可推知自由基中間體的什麼立體性質？
2. **(10-39)** 將光學活性的 `(R)-2-chloropentane` 進行自由基氯化並分離出 `2,4-dichloropentane`。請問會生成幾個立體異構物？它們的比例是否為 1:1？是否具有旋光性？

<details>
<summary>💡 點擊展開答案與詳解</summary>

1. **10-38 解析（原有的對掌中心被破壞）**：
   - `3-bromo-3-methylhexane` 的 C3 接有 $-\text{Br}, -\text{CH}_3, -\text{CH}_2\text{CH}_3, -\text{CH}_2\text{CH}_2\text{CH}_3$ 四個不同基團，因此**分子本身具有手性（chiral）**！
   - 產物不具旋光性是因為生成了 **50:50 的 $(R)/(S)$ 外消旋混合物**。這證明三級自由基中間體是 **$sp^2$ 平面結構（planar and achiral）**，$\text{Br}_2$ 從平面上方與下方攻擊的機率完全相等（各 50%）。

2. **10-39 解析（原有的 C2 對掌中心保留，在 C4 產生新立體中心）**：
   - 起始物是純的 `(2R)-2-chloropentane`。當發生 C4 氯化時，**C2 的 $\text{C–Cl}$ 鍵完全沒有斷裂，依然維持 100% 的 $(2R)$ 構型**！
   - 在 C4 產生的平面自由基從兩面受攻擊，分別形成 $(4R)$ 與 $(4S)$ 兩種構型：
     - **產物 1**：**(2R,4R)-2,4-dichloropentane**（**具手性且具旋光性**！因為現場完全沒有它的對映異構物 $(2S,4S)$！）
     - **產物 2**：**(2R,4S)-2,4-dichloropentane**（這是內消旋化合物 **meso**，有對稱面，因此**不具旋光性**）。
   - **比例**：這兩個產物互為**非對映異構物（diastereomers）**，過渡態能量不同，因此生成的比例**不等於 1:1**！
</details>

---

### - [ ] 5. Problem 10-34 & 10-37 (pp. 308e, 308f) ⭐⭐ 【自由基穩定度排序與共振結構】
**題目重點**：
1. **(10-34)** 將課本 p. 308e 的三組自由基依穩定度**由高到低（most stable to least stable）**排序：
   - (a) ① 內部二級丙烯基自由基（allylic）、② 末端一級孤立自由基、③ 雙鍵上的乙烯基自由基（vinylic）
   - (b) 環己二烯／環己烯相關自由基：① 孤立二級自由基、② 單雙鍵鄰位的 allylic 自由基、③ 夾在兩個雙鍵中間的雙重 allylic（pentadienyl）自由基
   - (c) `2-methylpentane` 上的三種自由基：① $2^\circ$ 自由基、② $3^\circ$ 自由基、③ $1^\circ$ 自由基
2. **(10-36 & 10-37)** 畫出苄基自由基（benzyl radical, $\text{Ph}\dot{\text{C}}\text{H}_2$）的共振結構。

<details>
<summary>💡 點擊展開答案與詳解</summary>

1. **10-34 自由基穩定度排序（通則：共軛共振 $>$ 單純 allylic / benzylic $> 3^\circ > 2^\circ > 1^\circ >$ vinylic）**：
   - **(a)** **第 1 個（allylic 自由基，具共振穩定）$>$ 第 2 個（孤立 $1^\circ$ 自由基）$>$ 第 3 個（vinylic 自由基，$sp^2$ 碳電負度高最不穩定）**。
   - **(b)** **第 2 個（夾在兩雙鍵間，可共振至 3 個碳）$>$ 第 3 個（單一雙鍵鄰位 allylic，共振至 2 個碳）$>$ 第 1 個（孤立 $2^\circ$ 自由基，無共振）**。
   - **(c)** **第 2 個（$3^\circ$ 自由基）$>$ 第 1 個（$2^\circ$ 自由基）$>$ 第 3 個（$1^\circ$ 自由基）**。
2. **10-36 苄基自由基共振結構**：
   - 共有 **4 個共振結構**：單電子除了在環外的 $-\dot{\text{C}}\text{H}_2$ 上，還可透過單電子魚鉤箭頭（fishhook arrows）共振分散到苯環的**兩個鄰位（ortho）**與**一個對位（para）**碳上。
</details>

---

## 第三部分：NBS 丙烯位／苄位溴化與合成陷阱（3 題）

### - [ ] 6. Problem 10-18 & 10-19 (p. 308b) ⭐⭐⭐ 【NBS 丙烯位溴化機構＆NBS 產生 Br2 的原因】
**題目重點**：
1. **(10-18a,c)** 畫出 `cyclohexene` 與 `1-butene` 進行 NBS 丙烯位溴化的兩個鏈增長步驟（Propagation steps，使用 $\text{Br}\cdot$ 與 $\text{Br}_2$）。
2. **(10-19)** NBS 為何能提供低濃度的 $\text{Br}_2$？畫出 $\text{NBS} + \text{HBr} \rightarrow \text{Iminol intermediate} + \text{Br}_2 \xrightarrow{\text{HBr}} \text{Succinimide}$ 的雙電子箭頭機構。

<details>
<summary>💡 點擊展開答案與詳解</summary>

1. **10-18 鏈增長兩步驟（使用單電子魚鉤箭頭 $\rightharpoonup$）**：
   - **Step 1（拔氫形成 Allylic radical）**：$\text{Br}\cdot$ 拔取雙鍵鄰位（allylic）的氫原子，生成 $\text{HBr}$ 與共振穩定的**丙烯基自由基（allylic radical）**。
   - **Step 2（與 $\text{Br}_2$ 反應）**：丙烯基自由基與低濃度的 $\text{Br–Br}$ 反應，生成丙烯基溴（allylic bromide）並再生一個 $\text{Br}\cdot$ 繼續循環。
     *(注意：在 10-18c 中，`1-butene` 的不對稱丙烯基自由基有 $\text{CH}_3\text{CH=CH}-\dot{\text{C}}\text{H}_2 \leftrightarrow \text{CH}_3\dot{\text{C}}\text{H}-\text{CH=CH}_2$ 兩個共振端點，課本畫出在末端反應生成 `1-bromo-2-butene` 的路徑)*。
2. **10-19 NBS 產生 $\text{Br}_2$ 的極性機構（雙電子箭頭 $\rightarrow$）**：
   - **第一階段（生成 $\text{Br}_2$）**：NBS 的羰基氧先被 $\text{HBr}$ 的 $\text{H}^+$ 質子化（活化 $\text{N–Br}$ 鍵），接著 $\text{Br}^-$ 親核攻擊 $\text{N–Br}$ 上的溴原子，將電子推回氮—碳鍵形成 $\text{C=N}$ 雙鍵，釋放出 **$\text{Br}_2$** 並形成 **Iminol 中間體**。
   - **第二階段（互變異構化為 Succinimide）**：類似酮—烯醇互變異構，Iminol 的氮原子被 $\text{HBr}$ 質子化，同時 $\text{Br}^-$ 拔去 $-\text{OH}$ 上的質子，電子推回形成 $\text{C=O}$ 雙鍵，得到副產物 **Succinimide（丁二醯亞胺）**。
</details>

---

### - [ ] 7. Problem 10-27 & 10-28 (p. 308d) ⭐⭐⭐ 【NBS 合成陷阱：不對稱丙烯基自由基】
**題目重點**：
1. **(10-27)** 某化學家想用 `2-pentene` + $\text{NBS} / h\nu$ 來大量製備 `1-bromo-2-pentene`，這個計畫有什麼嚴重問題？會產生哪些副產物？
2. **(10-28)** `1-methylcyclohexene` 與 NBS 反應會得到哪些產物？適合作為合成步驟嗎？

<details>
<summary>💡 點擊展開答案與詳解</summary>

**核心鐵則**：NBS 溴化只有在**丙烯基自由基中間體完全對稱（或只有單一反應位點）**時才適合用於合成！
1. **10-27 (`2-pentene` + NBS) 的兩大問題**：
   - **問題一（兩種不同的 allylic H 可被拔除）**：C1（甲基）與 C4（亞甲基）都是雙鍵鄰位！拔除 C4 的 H（$2^\circ$ allylic，甚至更快！）會產生 C2–C3–C4 自由基；拔除 C1 的 H 則產生 C1–C2–C3 自由基。
   - **問題二（不對稱自由基共振給兩種位置異構物）**：
     - 由 C1 拔氫形成的自由基（$\dot{\text{C}}\text{H}_2-\text{CH=CHCH}_2\text{CH}_3 \leftrightarrow \text{CH}_2\text{=CH}-\dot{\text{C}}\text{HCH}_2\text{CH}_3$）會給出目標物 `1-bromo-2-pentene` 與副產物 **`3-bromo-1-pentene`**。
     - 由 C4 拔氫形成的自由基（$\text{CH}_3\text{CH=CH}-\dot{\text{C}}\text{H}-\text{CH}_3 \leftrightarrow \text{CH}_3\dot{\text{C}}\text{H}-\text{CH=CHCH}_3$，此自由基剛好對稱）則會給出大量的副產物 **`4-bromo-2-pentene`**！
2. **10-28 (`1-methylcyclohexene` + NBS)**：
   - 共有 3 個不同的 allylic 位置（環外甲基、C3、C6），且拔除 C3 或 C6 的 H 都會形成不對稱的環內丙烯基自由基，最終會產生 **4 種不同溴代烯的位置異構物大雜燴**（`3-bromo-1-methylcyclohexene`、`6-bromo-1-methylcyclohexene`、`3-bromo-3-methylcyclohexene`、`1-(bromomethyl)cyclohexene`），**完全不適合用於合成**！
</details>

---

### - [ ] 8. Problem 10-29 & 10-30 (p. 308d) ⭐⭐⭐ 【NBS 的特殊高選擇性：共軛驅動力】
**題目重點**：
1. **(10-29)** `1,4-hexadiene`（$\text{CH}_3\text{CH=CH-CH}_2\text{-CH=CH}_2$）與 NBS 反應時，最穩定的自由基中間體結構為何？會得到什麼產物？
2. **(10-30)** `1-phenyl-2-butene`（$\text{Ph-CH}_2\text{-CH=CH-CH}_3$）與 NBS 反應主要得到什麼產物？為什麼？

<details>
<summary>💡 點擊展開答案與詳解</summary>

1. **10-29 (`1,4-hexadiene` + NBS)**：
   - **最穩定的自由基中間體**：拔除夾在兩個雙鍵正中間 **C3（$-\text{CH}_2-$）** 上的氫！因為這會形成能夠同時與左右兩個雙鍵共振的**五碳共軛自由基（pentadienyl-type radical）**，單電子分散在 C1、C3、C5 三個碳上，穩定度遠高於只拔 C6 甲基氫。
   - **產物**：$\text{Br}_2$ 優先攻擊產生**共軛雙鍵（conjugated diene，比孤立雙鍵穩定得多）**的 C1 與 C5 端點，主要生成 **`1-bromo-2,4-hexadiene`** 與 **`5-bromo-1,3-hexadiene`**（外加少量非共軛的 `3-bromo-1,4-hexadiene`）。
2. **10-30 (`1-phenyl-2-butene` + NBS)**：
   - **拔氫位置**：C1（$\text{Ph}-\text{CH}_2-\text{CH=CHCH}_3$）同時處於**苯環鄰位（benzylic）**與**雙鍵鄰位（allylic）**！拔除 C1 的 H 所形成的自由基同時享有苯環與雙鍵的共振穩定（$\text{Ph}-\dot{\text{C}}\text{H}-\text{CH=CHCH}_3 \leftrightarrow \text{Ph}-\text{CH=CH}-\dot{\text{C}}\text{HCH}_3$）。
   - **主要產物**：兩個共振位置中，當 $-\text{Br}$ 接在 C3 時，雙鍵可以與苯環形成**共軛體系（conjugated with the benzene ring）**，熱力學上最穩定，故主要產物為 **`3-bromo-1-phenyl-1-butene`**（$\text{Ph-CH=CH-CH(Br)CH}_3$，以及部分 `1-bromo-1-phenyl-2-butene`）。
</details>

---

## 第四部分：反應機構、氧化態判斷與醇轉鹵代烷（3 題）

### - [ ] 9. Problem 10-26 & 10-49 (pp. 308d, 308h) ⭐⭐ 【第 10 章核心反應總覽與醇反應速率】
**題目重點**：
1. **(10-26)** 預測下列反應的產物：
   - (a) `1-methylcyclopentanol` + $\text{HBr, ether}$
   - (b) `1-butanol` + $\text{SOCl}_2$
   - (c) `cyclohexene` + $\text{NBS}, h\nu, \text{CCl}_4$
   - (d) `cyclopentanol` + $\text{PBr}_3, \text{ether}$
   - (e) `2-bromobutane` $\xrightarrow{\text{Mg, ether}} \mathbf{A} \xrightarrow{\text{H}_2\text{O}} \mathbf{B}$
   - (f) `1-bromobutane` $\xrightarrow{\text{Li, pentane}} \mathbf{A} \xrightarrow{\text{CuI}} \mathbf{B}$
   - (g) `1-bromobutane` + $(\text{CH}_3)_2\text{CuLi} \xrightarrow{\text{ether}} ?$
2. **(10-49)** 比較下列各組醇與 $\text{HX}$ 反應生成鹵代烷的速率快慢：
   - (a) `1-butanol` vs. `2-propanol`
   - (b) `1-methylcyclopentanol` vs. `2-methylcyclopentanol`

<details>
<summary>💡 點擊展開答案與詳解</summary>

1. **10-26 產物**：
   - **(a)** `1-bromo-1-methylcyclopentane`（$3^\circ$ 醇與 $\text{HBr}$ 快速走 $\text{S}_\text{N}1$）。
   - **(b)** `1-chlorobutane`（$1^\circ$ 醇用 $\text{SOCl}_2$ 轉為氯代烷）。
   - **(c)** `3-bromocyclohexene`（對稱環烯 NBS 丙烯位溴化得單一產物）。
   - **(d)** `bromocyclopentane`（$2^\circ$ 醇用 $\text{PBr}_3$ 轉為溴代烷）。
   - **(e)** **A** = `sec-butylmagnesium bromide` ($\text{CH}_3\text{CH}_2\text{CH(MgBr)CH}_3$)；**B** = `butane` ($\text{CH}_3\text{CH}_2\text{CH}_2\text{CH}_3$)。
   - **(f)** **A** = `butyllithium` ($\text{CH}_3\text{CH}_2\text{CH}_2\text{CH}_2\text{Li}$)；**B** = `lithium dibutylcopper` [$(\text{CH}_3\text{CH}_2\text{CH}_2\text{CH}_2)_2\text{CuLi}$，Gilman 試劑]。
   - **(g)** `pentane`（$\text{CH}_3\text{CH}_2\text{CH}_2\text{CH}_2\text{CH}_3$，Gilman 偶聯延長 1 個碳）。
2. **10-49 與 HX 反應速率（通則：$3^\circ > 2^\circ > 1^\circ$，取決於碳陽離子穩定度）**：
   - **(a)** **`2-propanol` ($2^\circ$) 較快**（優於 $1^\circ$ 的 `1-butanol`）。
   - **(b)** **`1-methylcyclopentanol` ($3^\circ$) 較快**（優於 $2^\circ$ 的 `2-methylcyclopentanol`）。
</details>

---

### - [ ] 10. Problem 10-21 (p. 308b) ⭐⭐ 【三丁基氫化錫自由基脫鹵還原機構】
**題目重點**：鹵代烷（$\text{R–X}$）可與三丁基氫化錫（$\text{Bu}_3\text{SnH}$）在光照（$h\nu$）下透過自由基連鎖反應還原為烷類（$\text{R–H} + \text{Bu}_3\text{SnX}$）。已知鏈起始步為 $\text{Bu}_3\text{Sn–H}$ 均裂產生 $\text{Bu}_3\text{Sn}\cdot$，請畫出兩個鏈增長步驟（Propagation steps）的魚鉤箭頭機構。

<details>
<summary>💡 點擊展開答案與詳解</summary>

- **Initiation（鏈起始）**：
  $$\text{Bu}_3\text{Sn–H} \xrightarrow{h\nu} \text{Bu}_3\text{Sn}\cdot + \text{H}\cdot$$
- **Propagation（鏈增長兩步，皆畫單電子魚鉤箭頭 $\rightharpoonup$）**：
  1. **Step 1（錫自由基拔除鹵素 X）**：$\text{Bu}_3\text{Sn}\cdot$ 攻擊 $\text{R–X}$ 的鹵素原子，$\text{C–X}$ 鍵均裂，形成強健的 $\text{Bu}_3\text{Sn–X}$ 鍵與**烷基自由基 $\text{R}\cdot$**：
     $$\text{Bu}_3\text{Sn}\cdot + \text{R–X} \longrightarrow \text{Bu}_3\text{Sn–X} + \text{R}\cdot$$
  2. **Step 2（烷基自由基從 $\text{Bu}_3\text{SnH}$ 拔氫）**：$\text{R}\cdot$ 攻擊另一分子微弱的 $\text{Bu}_3\text{Sn–H}$ 鍵，生成還原產物 **$\text{R–H}$** 並再生 **$\text{Bu}_3\text{Sn}\cdot$** 繼續連鎖循環：
     $$\text{R}\cdot + \text{Bu}_3\text{Sn–H} \longrightarrow \text{R–H} + \text{Bu}_3\text{Sn}\cdot$$
</details>

---

### - [ ] 11. Problem 10-31, 10-32 & 10-33 (p. 308e) ⭐⭐ 【有機分子的氧化態排序與氧化還原判斷】
**題目重點**：
1. **(10-31b)** 將下列四個三碳分子依氧化態**由低到高（increasing oxidation level）**排列：
   `1-propanamine` ($\text{CH}_3\text{CH}_2\text{CH}_2\text{NH}_2$)、`1-bromopropane` ($\text{CH}_3\text{CH}_2\text{CH}_2\text{Br}$)、`1-chloro-2-propanone` ($\text{CH}_3\text{COCH}_2\text{Cl}$)、`1-bromo-3-chloropropane` ($\text{BrCH}_2\text{CH}_2\text{CH}_2\text{Cl}$)。
2. **(10-33)** 判斷下列三個反應屬於**氧化（oxidation）**、**還原（reduction）**，還是**非氧化還原（neither）**？
   - (a) $\text{CH}_3\text{CH}_2\text{OH} \xrightarrow{\text{CrO}_3} \text{CH}_3\text{CHO}$
   - (b) $\text{H}_2\text{C=CHCOCH}_3 + \text{NH}_3 \longrightarrow \text{H}_2\text{NCH}_2\text{CH}_2\text{COCH}_3$
   - (c) `2-bromobutane` $\xrightarrow{1.\ \text{Mg} / 2.\ \text{H}_2\text{O}}$ `butane`

<details>
<summary>💡 點擊展開答案與詳解</summary>

**快速計算法**：計算分子中**碳與高電負度雜原子（$\text{O, N, X}$）的總鍵數 + $\pi$ 鍵數**（或每多一個 $\text{C–Z}$ 鍵記 $+1$，每多一個 $\text{C–H}$ 鍵記 $-1$）：
1. **10-31(b) 氧化態排序**：
   - `1-propanamine` 與 `1-bromopropane`：都只有 **1 個 $\text{C–Z}$ 單鍵** $\rightarrow$ **氧化態並列最低**！
   - `1-bromo-3-chloropropane`：有 **2 個 $\text{C–Z}$ 單鍵**（1 個 C–Br、1 個 C–Cl）$\rightarrow$ **居中**。
   - `1-chloro-2-propanone`：有 **3 個 $\text{C–Z}$ 鍵**（$\text{C=O}$ 算 2 個 + 1 個 $\text{C–Cl}$）$\rightarrow$ **氧化態最高**！
   - **排序**：$\text{CH}_3\text{CH}_2\text{CH}_2\text{NH}_2 = \text{CH}_3\text{CH}_2\text{CH}_2\text{Br} < \text{BrCH}_2\text{CH}_2\text{CH}_2\text{Cl} < \text{CH}_3\text{COCH}_2\text{Cl}$。
2. **10-33 反應判斷**：
   - **(a) Oxidation（氧化）**：乙醇脫去 2 個 H 變成乙醛（$\text{C–O}$ 鍵由 1 變 2）。
   - **(b) Neither（非氧化還原）**：這只是將 $\text{H–NH}_2$ 加成到雙鍵上（一個碳多 1 個 $\text{C–H}$ 鍵 $-1$，另一個碳多 1 個 $\text{C–N}$ 鍵 $+1$，總氧化態完全沒變！類比於烯類加水 $\text{H}_2\text{O}$ 或加 $\text{HX}$）。
   - **(c) Reduction（還原）**：$\text{C–Br}$ 鍵被換成 $\text{C–H}$ 鍵，碳的電子密度增加，屬於還原反應。
</details>

---

## 第五部分：有機金屬（Grignard / Gilman / Suzuki）合成與除錯壓軸題（4 題）

### - [ ] 12. Problem 10-41 & 10-42 (p. 308f) ⭐⭐⭐⭐ 【有機金屬與鹵化合成找碴必考題】
**題目重點**：
1. **(10-41)** 下列三個合成反應都無法順利進行，請指出原因：
   - (a) $\text{CH}_3\text{CH}_2\text{CH}_2\text{F} \xrightarrow{1.\ \text{Mg} / 2.\ \text{H}_3\text{O}^+} \text{CH}_3\text{CH}_2\text{CH}_3$
   - (b) `1-methyl-3-methylenecyclohexane` $\xrightarrow{\text{NBS}, h\nu, \text{CCl}_4}$ 只在 C2 溴化
   - (c) `fluorocyclohexane` + $(\text{CH}_3)_2\text{CuLi} \xrightarrow{\text{ether}}$ `methylcyclohexane`
2. **(10-42)** 為什麼無法從 `4-bromo-1-pentanol`（$\text{CH}_3\text{CH(Br)CH}_2\text{CH}_2\text{CH}_2\text{OH}$）與 $\text{Mg}$ 反應製備 Grignard 試劑？

<details>
<summary>💡 點擊展開答案與詳解</summary>

1. **10-41 失敗原因**：
   - **(a) 氟代烷不形成 Grignard 試劑**：$\text{C–F}$ 鍵太強，烷基氟化物（alkyl fluorides）幾乎無法與金屬鎂（$\text{Mg}$）反應生成 Grignard 試劑（必須改用 $-\text{Cl}, -\text{Br}, -\text{I}$）。
   - **(b) NBS 丙烯位溴化產生多種異構物**：環外雙鍵兩側的 C2 與 C4 都是 allylic 位置，且各自形成的丙烯基自由基皆不對稱（還可共振到環外 $=\text{CH}_2$ 碳上！），會產生至少 4 種不同溴代產物的混合物。
   - **(c) 氟代烷不參與 Gilman 偶聯**：Gilman 試劑（$\text{R}_2\text{CuLi}$）只能與氯、溴、碘代物（$\text{R}'–\text{Cl}, \text{Br}, \text{I}$）偶聯，**氟代烷（$\text{R}'–\text{F}$）不反應**！
2. **10-42 失敗原因（分子內酸鹼自毀）**：
   - Grignard 試劑（$\text{RMgBr}$）是極強的鹼（共軛酸 $\text{p}K_\text{a} \approx 50$），而同一分子末端的醇羥基（$-\text{OH}$，$\text{p}K_\text{a} \approx 16$）具有酸性氫！
   - 一旦 $\text{C–Br}$ 與 $\text{Mg}$ 形成 $-\text{MgBr}$，它會立刻拔取分子內（或鄰近分子）$-\text{OH}$ 上的質子 $\text{H}^+$，直接變成 `1-pentanol` 的鎂鹽（$\text{CH}_3\text{CH}_2\text{CH}_2\text{CH}_2\text{CH}_2\text{OMgBr}$）。其他如含 $-\text{NH}_2$、$-\text{CO}_2\text{H}$、$-\text{SH}$、$-\text{C}\equiv\text{CH}$ 的鹵代物也同樣無法直接製備 Grignard 試劑。
</details>

---

### - [ ] 13. Problem 10-25 & 10-40 (pp. 308c, 308f) ⭐⭐⭐ 【有機金屬偶聯與多步合成設計】
**題目重點**：
1. **(10-25)** 以環戊烯（`cyclopentene`）為起始物，如何合成：(b) `methylcyclopentane`、(e) `cyclopentylcyclopentane`（聯環戊烷）、(f) `1,3-cyclopentadiene`？
2. **(10-40)** 如何分別從 (1) `cyclohexene`、(2) `cyclohexanol`、(3) `cyclohexane` 出發，合成出正丙基環己烷（`propylcyclohexane`）？

<details>
<summary>💡 點擊展開答案與詳解</summary>

1. **10-25 合成路線**：
   - **(b) `methylcyclopentane`（兩步）**：
     1. `HBr, ether` $\rightarrow$ `bromocyclopentane`
     2. `(CH3)2CuLi, ether`（Gilman 偶聯接上甲基！）
   - **(e) `cyclopentylcyclopentane`（三步）**：
     1. `HBr, ether` $\rightarrow$ `bromocyclopentane`
     2. 取一部分與 `1. 2 Li, pentane; 2. CuI, ether` 製備成二環戊基銅鋰 `(cyclopentyl)2CuLi`
     3. 再與另一部分 `bromocyclopentane` 偶聯即得聯環戊烷！
   - **(f) `1,3-cyclopentadiene`（兩步）**：
     1. `NBS, hν, CCl4` $\rightarrow$ `3-bromocyclopentene`
     2. `KOH, ethanol`（或 `NaNH2` / 強鹼進行 E2 消去脫去 $\text{HBr}$）$\rightarrow$ `1,3-cyclopentadiene`！
2. **10-40 合成 `propylcyclohexane`**：
   - **關鍵**：只要先把這三個起始物都轉變成 **`bromocyclohexane`（或 `chlorocyclohexane`）**，最後統一加上二丙基銅鋰 **`(CH3CH2CH2)2CuLi, ether`** 偶聯即可！
   - (1) 從 `cyclohexene`：`HBr, ether` $\rightarrow$ `bromocyclohexane` $\xrightarrow{(\text{CH}_3\text{CH}_2\text{CH}_2)_2\text{CuLi}}$ `propylcyclohexane`。
   - (2) 從 `cyclohexanol`：`PBr3, ether`（或 `SOCl2, pyridine`）$\rightarrow$ `bromocyclohexane` $\xrightarrow{(\text{CH}_3\text{CH}_2\text{CH}_2)_2\text{CuLi}}$ `propylcyclohexane`。
   - (3) 從 `cyclohexane`：`Br2, hν`（或 `Cl2, hν`）$\rightarrow$ `bromocyclohexane` $\xrightarrow{(\text{CH}_3\text{CH}_2\text{CH}_2)_2\text{CuLi}}$ `propylcyclohexane`。
</details>

---

### - [ ] 14. Problem 10-44 (p. 308g) ⭐⭐⭐ 【跨章三步合成填空】
**題目重點**：寫出 p. 308g 合成流程中的試劑 **a、b、c**：
`(E)-ethylidenecyclohexane` $\xrightarrow{\mathbf{a}}$ `1-cyclohexylethanol` $\xrightarrow{\mathbf{b}}$ `(1-bromoethyl)cyclohexane` $\xrightarrow{\mathbf{c}}$ `isopropylcyclohexane`

<details>
<summary>💡 點擊展開答案與詳解</summary>

- **a（Non-Markovnikov 水合）**：雙鍵一端是環上四取代碳，另一端是環外三取代碳（帶 H 與 $\text{CH}_3$）。因為 $-\text{OH}$ 加在取代基較少的環外碳上，必須使用**硼氫化氧化**：`1. BH3, THF; 2. H2O2, OH⁻`！
- **b（$2^\circ$ 醇轉為溴代烷且不重排！）**：因為該二級醇緊鄰六元環，若用 $\text{HBr}$ 極易發生碳陽離子重排（擴環或氫轉移），故必須使用 **`PBr3, ether`**！
- **c（溴代烷轉為甲基取代烷）**：使用 Gilman 試劑偶聯 **`(CH3)2CuLi, ether`**！
</details>

---

### - [ ] 15. Problem 10-47 & 10-50 (pp. 308g, 308h) ⭐⭐⭐⭐ 【Suzuki–Miyaura 鈀催化偶聯與催化循環壓軸題】
**題目重點**：
1. **(10-47b)** 如何利用 Suzuki–Miyaura 反應合成 `4'-methyl-[1,1'-biphenyl]-2-amine`（一環接鄰位 $-\text{NH}_2$，另一環接對位 $-\text{CH}_3$ 的聯苯）？畫出兩組可能的反應物組合，並說明為何此反應不需擔心 $-\text{NH}_2$ 的酸性氫（對比 Grignard / Gilman）？
2. **(10-50a)** 預測 `3-bromobenzoic acid` + `phenylboronic acid` 在 $\text{Pd(OAc)}_2$（與鹼）催化下的產物，並完整描述 Suzuki–Miyaura 催化循環的三個核心步驟。

<details>
<summary>💡 點擊展開答案與詳解</summary>

1. **10-47(b) 兩組反應物夥伴（在兩個苯環之間的單鍵切開，一邊放 $-\text{B(OH)}_2$、一邊放 $-\text{I}$ 或 $-\text{Br}$）**：
   - **組合一**：`2-iodoaniline`（鄰碘苯胺）$+$ `(4-methylphenyl)boronic acid`，催化劑 `Pd(PPh3)4, CaCO3, THF`。
   - **組合二**：`(2-aminophenyl)boronic acid` $+$ `1-iodo-4-methylbenzene`，催化劑 `Pd(PPh3)4, CaCO3, THF`。
   - **優勢**：有機硼酸（$\text{R–B(OH)}_2$）共價性強、鹼性極弱，不會像 Grignard（$\text{RMgX}$）或 Gilman（$\text{R}_2\text{CuLi}$）那樣被 $-\text{NH}_2$、$-\text{CO}_2\text{H}$、$-\text{CO}_2\text{CH}_3$ 等官能基質子化破壞！
2. **10-50(a) 產物與催化循環三步驟**：
   - **產物**：**[1,1'-biphenyl]-3-carboxylic acid**（3-苯基苯甲酸，原本 $-\text{Br}$ 的位置被換成 $-\text{Ph}$，而 $-\text{CO}_2\text{H}$ 完好保留）。
   - **$\text{Pd}(0)$ 催化循環三步驟**：
     1. **Oxidative Addition（氧化加成）**：活性催化劑 $\text{Pd}(0)\text{L}_2$ 插入芳基溴（$\text{Ar–Br}$）的碳—溴鍵，鈀由 0 價氧化為 $+2$ 價，形成 **$\text{Ar–Pd(II)(L)}_2\text{–Br}$**。
     2. **Transmetallation（轉金屬化）**：在鹼（如 $\text{OH}^-$ 或 $\text{CO}_3^{2-}$ 活化硼酸形成四配位硼酸根 $\text{PhB(OH)}_3^-$）協助下，苯基從硼轉移到鈀上（取代 $\text{Br}^-$），形成二芳基鈀中間體 **$\text{Ar–Pd(II)(L)}_2\text{–Ph}$**。
     3. **Reductive Elimination（還原消去）**：兩個芳基在鈀中心偶聯形成新的碳—碳鍵，釋放聯苯產物 **$\text{Ar–Ph}$**，同時鈀由 $+2$ 價還原回 **$\text{Pd}(0)\text{L}_2$** 進入下一輪循環。
</details>
