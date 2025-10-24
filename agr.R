df_agri <- data.frame(
ID <- c(1: 30, 15, 31, 34, 17, 32, 17, 35, 36, 37, 38) ;
Region <- c("Nord", "Sud", "Est", "Ouest", "Nord", "Sud", "Est", "Ouest", "Nord", "Sud","Est", "
Ouest", "Nord", "Sud", "Est", "Ouest", "Nord", "Sud", "Est", "Ouest","Est", "
Ouest", "Nord", "Sud", "Est"),
Culture <- c("Blé", "Maïs", "Orge", "Colza", "Tournesol", "Blé", "Maïs", "Orge", "Colza", "Tourneso
l","Blé", "Maïs", "Orge", "Colza", "Tournesol", "Blé", "Maïs", "Orge", "Colza",
"Tournesol","Orge", "Colza", "Blé", "Maïs", "Tournesol"),
Surface <- round(c(15.5, 22.3, 18.7, 12.8, 25.1, 14.2, 20.8, 17.3, 11.5, 23.7, 16.8, 21.5, 19.2
, 13.1, 24.8, 15.1, 22.7, 18.1, 12.3, 25.5, 18.1, 12.3, 14.9, 21.2, 24.1)),
Production <- round(c(6.2, 8.5, 7.1, 4.8, 9.3, 5.8, 7.9, 6.7, 4.2, 8.8, 6.5, 8.2, 7.3, 4.9, 9.1
, 6.1, 8.4, 7.0, 4.5, 9.0, 7.0, 4.5, 5.9, 8.1, 8.9), 1),
Irrigation <- c("Oui", "Non", "Oui", "Non", "Oui", "Non", "Oui", "Non", "Oui", "Non", "Oui", "N
on", "Oui", "Non", "Oui", "Non", "Oui", "Non", "Oui", "Non", "Non", "Oui", "No
n", "Oui", "Non"),
)