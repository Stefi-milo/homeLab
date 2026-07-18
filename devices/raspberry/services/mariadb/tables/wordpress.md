MariaDB [wordpress]> show tables;
+----------------------------------------------+
| Tables_in_wordpress                          |
+----------------------------------------------+
| wordpress1actionscheduler_actions            |
| wordpress1actionscheduler_claims             |
| wordpress1actionscheduler_groups             |
| wordpress1actionscheduler_logs               |
| wordpress1anc_6310_counter                   |
| wordpress1anc_6310_icons                     |
| wordpress1anc_6310_style                     |
| wordpress1commentmeta                        |
| wordpress1comments                           |
| wordpress1hfcm_scripts                       |
| wordpress1links                              |
| wordpress1medals                             |
| wordpress1nextend2_image_storage             |
| wordpress1nextend2_section_storage           |
| wordpress1nextend2_smartslider3_generators   |
| wordpress1nextend2_smartslider3_sliders      |
| wordpress1nextend2_smartslider3_sliders_xref |
| wordpress1nextend2_smartslider3_slides       |
| wordpress1options                            |
| wordpress1postmeta                           |
| wordpress1posts                              |
| wordpress1poststats_visits                   |
| wordpress1pvc_daily                          |
| wordpress1pvc_total                          |
| wordpress1snippets                           |
| wordpress1statistics_events                  |
| wordpress1statistics_exclusions              |
| wordpress1statistics_historical              |
| wordpress1statistics_pages                   |
| wordpress1statistics_useronline              |
| wordpress1statistics_visitor                 |
| wordpress1statistics_visitor_relationships   |
| wordpress1term_relationships                 |
| wordpress1term_taxonomy                      |
| wordpress1termmeta                           |
| wordpress1terms                              |
| wordpress1usermeta                           |
| wordpress1users                              |
| wp_medals                                    |
+----------------------------------------------+
39 rows in set (0.000 sec)

MariaDB [wordpress]> describe wp_medals;
+--------+---------+------+-----+---------+----------------+
| Field  | Type    | Null | Key | Default | Extra          |
+--------+---------+------+-----+---------+----------------+
| id     | int(11) | NO   | PRI | NULL    | auto_increment |
| cups   | int(11) | NO   |     | NULL    |                |
| gold   | int(11) | NO   |     | NULL    |                |
| silver | int(11) | NO   |     | NULL    |                |
| bronze | int(11) | NO   |     | NULL    |                |
+--------+---------+------+-----+---------+----------------+
5 rows in set (0.001 sec)
