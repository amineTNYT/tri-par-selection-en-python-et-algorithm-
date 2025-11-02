

### Description Détaillée du Tri par Sélection

**Tri par sélection**
Algorithme de tri **instable** et de complexité quadratique O(n²). Son principe est simple : à chaque étape, il sélectionne le plus petit élément restant dans la partie non triée et le place directement à sa position finale.

**Fonctionnement**
L'algorithme opère **en place** avec deux boucles imbriquées. Il divise virtuellement le tableau en deux parties : une partie gauche triée (initialement vide) et une partie droite non triée. À chaque itération, la partie triée s'agrandit d'un élément.

**Tableau initial :**
`t = [8, 77, 1]`

**Étape 1 :**
- Cherche le plus petit élément dans `[8, 77, 1]` → trouve `1` à la position 2
- Échange `8` et `1`
- Résultat : `[1, 77, 8]`

**Étape 2 :**
- Cherche le plus petit élément dans `[77, 8]` → trouve `8` à la position 2
- Échange `77` et `8`
- Résultat : `[1, 8, 77]`

**Tableau trié :**
`t = [1, 8, 77]`


https://github.com/user-attachments/assets/ebd35f58-287f-484c-9544-b39670498db3

**Note Importante sur la Variable `aux` :**

La déclaration de `aux` **dépend du type des éléments dans le tableau `t`**.

Si `t` contient :
- **Entiers** → `aux` doit être `entier`
- **Caractères** → `aux` doit être `caractère`
- **Chaînes de caractères** → `aux` doit être `chaine`
- **Nombres réels** → `aux` doit être `réel`
- **Objets personnalisés** → `aux` doit correspondre au type d'objet

**Exemple :**
```pascal
// Pour un tableau d'entiers
aux: entier

// Pour un tableau de caractères
aux: caractère

// Pour un tableau de nombres réels
aux: réel
```

**Toujours déclarer `aux` avec le même type de données que les éléments du tableau** pour éviter les erreurs de type lors des opérations d'échange.

