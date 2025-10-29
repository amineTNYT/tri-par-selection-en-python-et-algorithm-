

### Description Détaillée du Tri par Sélection

Le tri par sélection est un algorithme de tri par comparaison, **instable** et de complexité quadratique. Son principe fondamental est de construire séquentiellement la séquence triée en sélectionnant itérativement le plus petit (ou le plus grand) élément restant dans le sous-tableau non trié et de le placer à sa position finale correcte.

L'algorithme procède en deux boucles imbriquées et opère *en place*, c'est-à-dire sans nécessiter de tableau auxiliaire. Il considère le tableau comme étant divisé en deux parties virtuelles : un préfixe (ou une partie gauche) qui est trié et un suffixe (ou une partie droite) qui reste à trier. Initialement, la partie triée est vide.

**Déroulement de l'algorithme :**

1.  **Boucle Externe (Index `i`)** : Cette boucle parcourt le tableau de l'indice `0` à l'avant-dernier indice (`n-2`). À chaque itération, l'indice `i` représente la position courante où le prochain plus petit élément doit être inséré. C'est la frontière entre la partie déjà triée (`[0, i-1]`) et la partie non triée (`[i, n-1]`).

2.  **Recherche du Minimum (Index `pMin`)** : Pour chaque position `i`, l'algorithme initialise un pointeur `pMin` (indice du minimum provisoire) à `i`. Une boucle interne, avec l'indice `j`, parcourt ensuite le sous-tableau non trié, de `i+1` à `n-1`. Pour chaque élément `t[j]`, s'il est inférieur à l'élément courant `t[pMin]`, `pMin` est mis à jour avec la valeur de `j`. À la fin de cette boucle interne, `pMin` contient l'indice du plus petit élément trouvé dans la partie non triée.

3.  **Échange (Permutation)** : Après la recherche du minimum, un échange est effectué entre l'élément à la position frontière `i` et l'élément à la position `pMin`. Cet échange place le plus petit élément trouvé à sa position définitive `i`. Une vérification conditionnelle (`si i ≠ pMin`) est souvent ajoutée pour optimiser l'algorithme en évitant un échange inutile lorsque le plus petit élément est déjà à sa place.

**Propriétés :**

*   **Complexité** : La recherche du minimum nécessite de parcourir des sous-tableaux de taille décroissante (`n-1`, `n-2`, ..., `1`). Le nombre total de comparaisons est donc `(n-1) + (n-2) + ... + 1 = n(n-1)/2`, ce qui donne une complexité en **O(n²)** dans tous les cas (meilleur, pire et moyen). Le nombre d'échanges est de **O(n)**, ce qui est un avantage si les écritures en mémoire sont coûteuses.
