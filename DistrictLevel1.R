x <- c(1, 2, 3, 4, 5)

library(readr)
library(dplyr)
library(ggplot2)

districts <- read_csv('../districts.csv')
districts


viz <- ggplot(data=districts, aes(x=District,y=Years)) +
  geom_bar(aes(fill=District),stat='identity') +
  theme(legend.position = "none", axis.text.x = element_text(angle = 45, hjust =1)) +
  labs(title='Middle School Language in Neighboring Districts', subtitle="Number of years considered 'Level 1'")
viz
