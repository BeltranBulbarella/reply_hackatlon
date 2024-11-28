# Full course_database with the new course data

course_database = {
    'Calcul Haute Performance': {
        'nofist_data': [
            {
                'Title': 'Electif de SG6',
                'Type': '2A Electif SG6',
                'Resource': 'HPC - Comprendre la partie mathématique',
                'Page Count': '14',
                'Category': 'Fiche 2024'
            },
            {
                'Title': 'Correction Exos MPI',
                'Type': 'Fiche 2023',
                'Resource': '',
                'Page Count': '1',
                'Category': 'Fiche 2023'
            },
            {
                'Title': 'Correction Exo OpenMP',
                'Type': 'Fiche 2023',
                'Resource': '',
                'Page Count': '1',
                'Category': 'Fiche 2023'
            },
            {
                'Title': 'Exercices partie Informatique',
                'Type': 'Fiche 2022',
                'Resource': '',
                'Page Count': '2',
                'Category': 'Fiche 2022'
            },
            {
                'Title': 'Sujet Partiel HPC (Info) 22/23',
                'Type': 'Annale 2024',
                'Resource': '',
                'Page Count': '0',
                'Category': 'Annale 2024'
            },
            {
                'Title': 'Partiel CHP 2023 Session 2 Partie Maths',
                'Type': 'Annale 2023',
                'Resource': '',
                'Page Count': '0',
                'Category': 'Annale 2023'
            },
            {
                'Title': 'Partiel CHP 2022 Partie Informatique',
                'Type': 'Annale 2022',
                'Resource': '',
                'Page Count': '3',
                'Category': 'Annale 2022'
            },
            {
                'Title': 'Partiel CHP 2022 Partie Math',
                'Type': 'Annale 2022',
                'Resource': '',
                'Page Count': '4',
                'Category': 'Annale 2022'
            },
            {
                'Title': 'TP4',
                'Type': 'Annale 2022',
                'Resource': '',
                'Page Count': '0',
                'Category': 'Annale 2022'
            },
            {
                'Title': 'Rapport TP2 2021-2022',
                'Type': 'Annale 2022',
                'Resource': '',
                'Page Count': '0',
                'Category': 'Annale 2022'
            },
            {
                'Title': 'Transcription partiel (session 2) HPC 2021',
                'Type': 'Annale 2021',
                'Resource': '',
                'Page Count': '8',
                'Category': 'Annale 2021'
            },
            {
                'Title': 'Transcription partiel HPC 2021',
                'Type': 'Annale 2021',
                'Resource': '',
                'Page Count': '9',
                'Category': 'Annale 2021'
            },
            {
                'Title': 'Exercices corrigés',
                'Type': 'Annale 2021',
                'Resource': '',
                'Page Count': '0',
                'Category': 'Annale 2021'
            },
            {
                'Title': 'TP2 - Calcul distribué en MPI4py',
                'Type': 'Annale 2021',
                'Resource': '',
                'Page Count': '3',
                'Category': 'Annale 2021'
            },
            {
                'Title': 'Correction Exos MPI (Partie Informatique)',
                'Type': 'Exercices ou TDs 2023',
                'Resource': '',
                'Page Count': '0',
                'Category': 'Exercices ou TDs 2023'
            }
        ],
        'student_feedback': [
            {
                'Name': 'Kab',
                'Description': "Le cours porte sur les processeurs et des concepts informatiques avancés.",
                'Difficulties': "Cours difficiles, mais l'examen est facile.",
                'Workload': "Les TP sont nombreux et peuvent être pénibles, mais j'ai validé sans bien connaître le cours.",
                'Exam Remarks': "Les sujets abordés en cours sont complexes, mais l'examen est plutôt simple.",
                'Recommendation': "Non, je ne le recommande pas.",
                'Other Remarks': "RAS."
            },
            {
                'Name': 'Victor Petit',
                'Description': "On découvre plusieurs techniques pour accélérer et paralléliser des calculs. Je ne connaissais pas le sujet et c'était cool.",
                'Difficulties': "Identiques aux précédents commentaires.",
                'Workload': "Les TP étaient plutôt sympas, j'ai bien aimé.",
                'Exam Remarks': "",
                'Recommendation': "C'est vrai, c'était agréable.",
                'Other Remarks': ""
            },
            {
                'Name': 'Louis Vialard',
                'Description': "La matière est stylée, mais pas forcément intéressante.",
                'Difficulties': "Les TP sont également difficiles.",
                'Workload': "Les TP ne sont pas faciles et demandent du travail supplémentaire, ce qui est agaçant. Mais l'examen est très simple (et disponible sur Nofist maintenant).",
                'Exam Remarks': "Toujours le même.",
                'Recommendation': "Pas vraiment.",
                'Other Remarks': ""
            },
            {
                'Name': 'Antoine Marras',
                'Description': "Découverte de la programmation parallèle à travers l'historique du fonctionnement des ordinateurs, aspects mathématiques de la parallélisation, calculs matriciels sur supercalculateurs. Utilisation d'OpenMP (un peu de C) et MPI (pyMPI donc Python). Application aux résolutions d'équations différentielles (maillage, etc.).",
                'Difficulties': "",
                'Workload': "TP complexes, peuvent être longs (accès à distance sur les supercalculateurs de Metz, donc on peut perdre du temps sur des problèmes de connexions).",
                'Exam Remarks': "Examen faisable.",
                'Recommendation': "Oui, pour ceux qui veulent comprendre le fonctionnement concret d'un supercalculateur, l'optimisation, et les calculs matriciels lourds. En revanche, si vous souhaitez coder longuement en C, passez votre chemin. Le code est plutôt à 'trous' et n'a pas vocation à programmer, mais à mettre en application les bibliothèques et les méthodes du cours.",
                'Other Remarks': "Les professeurs sont cools et prennent du temps pour aider pendant les TP."
            },
            {
                'Name': 'Nada',
                'Description': "Comme précédemment.",
                'Difficulties': "Cours difficiles, pas faciles à suivre. TP compliqués mais faisables. Les profs ne notent pas de la même manière (Vialle, en l'occurrence, est sévère sur la notation). Aucun TD, TP supplémentaire ou annale n'est donné pour s'entraîner pour le partiel.",
                'Workload': "Comme précédemment.",
                'Exam Remarks': "Pas de TD/annale. Du code à faire sur papier. Partiel faisable.",
                'Recommendation': "Non, fuyez. Il y a d'autres cours beaucoup plus intéressants que cet électif. En dehors des TP, qui étaient plutôt fun, le reste est ennuyeux à souhait.",
                'Other Remarks': ""
            },
            {
                'Name': 'Théo Brionnaud',
                'Description': "Comme précédemment.",
                'Difficulties': "Le cours se divise en deux parties : une partie Centrale où l'aspect mathématique est mis en avant, et une partie Supélec où l'on voit plein de techniques d'implémentation. Si vous avez des bases en C/C++, cette partie passe relativement bien, sinon cela peut vite devenir un peu douloureux. La partie mathématique était dure à suivre si l'on n'a vraiment aucun intérêt pour les maths.",
                'Workload': "Comme précédemment.",
                'Exam Remarks': "Se valide à peu près convenablement. Examen difficile.",
                'Recommendation': "La partie TP est sympa et la partie implémentation pratique aussi si on a des affinités pour le C. Sinon, c'est un cours assez lourd que je ne recommande pas si on cherche juste un électif facile à valider.",
                'Other Remarks': "Pas d'aménagement possible négociable avec Vialle pour ceux en S8 anticipés -> Obligation de passer le rattrapage."
            },
            {
                'Name': 'Emir',
                'Description': "Parallélisation de boucles for, calcul matriciel sur un cluster de calculateurs, etc.",
                'Difficulties': "Le professeur n'explique pas grand-chose, les cours sont assez difficiles, les TP aussi. Les encadrants ne sont pas forcément disponibles pour tout le monde, car il est plus urgent de traiter les problèmes de connexion aux clusters de Metz que d'expliquer à un étudiant ce qui lui est demandé.",
                'Workload': "TP à finir chez soi souvent. C'est l'électif que j'ai le plus révisé et où j'ai eu la pire note.",
                'Exam Remarks': "Se valide assez facilement si on comprend ce qu'on fait.",
                'Recommendation': "Absolument pas, je regrette mon choix et le temps passé à travailler ce cours. C'est un électif assez complexe et il faut vraiment être passionné et avoir de la patience pour suivre la pédagogie de l'électif.",
                'Other Remarks': "Électif très orienté Supélec."
            },
            {
                'Name': 'Titouan Lévêque',
                'Description': "Introduction aux calculs parallèles du point de vue pratique (comment réaliser un programme qui exécute plusieurs tâches en même temps) et théorique (comment découper un problème en morceaux pouvant être exécutés simultanément).",
                'Difficulties': "Les cours étaient un peu confus mais on s'en sort, surtout avec le livre qui permettait de rattraper ce qu'on n'avait pas compris et d'avoir quelques exercices. Les profs sont prêts à répondre aux questions. Les TP n'étaient pas faciles, avec quelques problèmes techniques et parfois un manque d'accompagnement, mais on finit par s'en sortir. Les profs de TP sont parfois un peu perdus à cause des cafouillages techniques, mais on peut discuter avec eux en cas de problèmes, ce qui aide pas mal.",
                'Workload': "Un peu de travail régulier pour comprendre le cours (pas toujours clair en classe mais jamais très compliqué et se fait facilement et rapidement avec le livre). Par contre, les TP devaient parfois se finir après le cours ou à la maison, ce qui est plutôt contraignant. Le partiel consiste en des exercices de base ; il se révise bien avec le livre et surtout avec ce qu'il y a sur Nofist (se ressemble d'une année sur l'autre).",
                'Exam Remarks': "Des exercices pas trop difficiles, en partie disponibles sur Nofist.",
                'Recommendation': "Seulement si le sujet vous intéresse (faire de l'informatique ou de la recherche qui demande de savoir faire du calcul parallèle). Sinon, vous risquez de vous ennuyer.",
                'Other Remarks': "Prévoir une bonne organisation du temps."
            },
            {
                'Name': 'Tom Bray',
                'Description': "Un cours très intéressant sur le calcul parallèle.",
                'Difficulties': "Le cours peut être un peu difficile à comprendre si vous ne maîtrisez pas les bases des algorithmes et des fonctions introduites, mais après c'est tout le temps pareil.",
                'Workload': "Préparez bien vos TP la veille pour les rendre à temps le jour même. Connaissez bien les fonctions utilisées et les méthodes de parallélisation et vous n'aurez pas beaucoup plus de temps à investir.",
                'Exam Remarks': "Partie informatique : il faut savoir utiliser toutes les fonctions sans trop de problème. Partie mathématiques : cela fait trois ans que c'est le même exercice : savoir conditionner une matrice sous forme de déterminant de Schur. Sachez le faire et vous avez au moins 10/20. Les TP comptent beaucoup pour la note aussi.",
                'Recommendation': "Oui, si vous aimez l'informatique.",
                'Other Remarks': ""
            }
        ],
        'language': 'French'
    }
}
