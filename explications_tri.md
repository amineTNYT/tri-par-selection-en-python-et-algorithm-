

### Description Détaillée du Tri par Sélection

Le tri par sélection est un algorithme de tri par comparaison, **instable** et de complexité quadratique. Son principe fondamental est de construire séquentiellement la séquence triée en sélectionnant itérativement le plus petit (ou le plus grand) élément restant dans le sous-tableau non trié et de le placer à sa position finale correcte.

L'algorithme procède en deux boucles imbriquées et opère *en place*, c'est-à-dire sans nécessiter de tableau auxiliaire. Il considère le tableau comme étant divisé en deux parties virtuelles : un préfixe (ou une partie gauche) qui est trié et un suffixe (ou une partie droite) qui reste à trier. Initialement, la partie triée est vide.

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

