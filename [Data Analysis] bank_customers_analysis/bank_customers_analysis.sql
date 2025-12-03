/*caricare il database banca*/

/* overview dei dati nelle varie tabelle */
SELECT * FROM banca.cliente;
SELECT * FROM banca.conto;
SELECT * FROM banca.tipo_conto;
SELECT * FROM banca.tipo_transazione;
SELECT * FROM banca.transazioni;

/* creo tabella temporanea per tutti i dati relativi alle transazioni*/
DROP TABLE IF EXISTS transazioni_info;
CREATE TEMPORARY TABLE transazioni_info AS
	SELECT *
	FROM banca.transazioni trans
	LEFT JOIN banca.tipo_transazione t_trans
	ON trans.id_tipo_trans = t_trans.id_tipo_transazione;

SELECT * FROM transazioni_info; /*visualizzo tabella creata*/
    
    
/* creo tabella temporanea per tutti i dati relativi ai conti e clienti*/
DROP TABLE IF EXISTS conti_info;
CREATE TEMPORARY TABLE conti_info AS
	SELECT 
    cl.id_cliente, 
    TIMESTAMPDIFF(YEAR, data_nAScita, CURRENT_DATE) AS eta,
    conto.id_conto, t_conto.*
	FROM banca.cliente cl
	LEFT JOIN banca.conto conto
	ON cl.id_cliente = conto.id_cliente
    
    LEFT JOIN banca.tipo_conto t_conto
	ON t_conto.id_tipo_conto = conto.id_tipo_conto;
  
SELECT * FROM conti_info; /*visualizzo tabella creata*/

    
/* creo tabella temporanea per aggregazioni sulle transazioni*/
DROP TABLE IF EXISTS trans_per_conto;
CREATE TEMPORARY TABLE trans_per_conto AS
	SELECT 
	id_conto, 
	COUNT(*) n_trans_tot,
	SUM(CASE WHEN segno = '+' THEN 1 ELSE 0 END) trans_entrata,
	SUM(CASE WHEN segno = '-' THEN 1 ELSE 0 END) trans_uscita,
	SUM(CASE WHEN segno = '+' THEN importo ELSE 0 END) importo_entrata,
	SUM(CASE WHEN segno = '-' THEN importo ELSE 0 END) importo_uscita
	FROM transazioni_info
	GROUP BY 1;

SELECT * FROM trans_per_conto; /*visualizzo tabella creata*/


/* creo tabella temporanea per aggregazioni sui conti*/
DROP TABLE IF EXISTS conti_per_cliente;
CREATE TEMPORARY TABLE conti_per_cliente AS
	SELECT 
	id_cliente,
	SUM(CASE WHEN id_conto IS NOT NULL THEN 1 ELSE 0 END) num_conti_tot,
	SUM(CASE WHEN id_tipo_conto = 0 THEN 1 ELSE 0 END) num_conti_base,
	SUM(CASE WHEN id_tipo_conto = 1 THEN 1 ELSE 0 END) num_conti_business,
	SUM(CASE WHEN id_tipo_conto = 2 THEN 1 ELSE 0 END) num_conti_priv,
	SUM(CASE WHEN id_tipo_conto = 3 THEN 1 ELSE 0 END) num_conti_fam
	FROM conti_info
	GROUP BY 1;

SELECT * FROM conti_per_cliente; /*visualizzo tabella creata*/


/* creo tabella temporanea per aggregazioni su transazioni per cliente per tipologia di conto*/
DROP TABLE IF EXISTS trans_per_cliente_per_conto;
CREATE TEMPORARY TABLE trans_per_cliente_per_conto AS
	SELECT 
	c.id_cliente,
	SUM(CASE WHEN id_tipo_conto = 0 and segno = '-' THEN 1 ELSE 0 END) t_uscita_c_base,
	SUM(CASE WHEN id_tipo_conto = 1 and segno = '-' THEN 1 ELSE 0 END) t_uscita_c_business,
	SUM(CASE WHEN id_tipo_conto = 2 and segno = '-' THEN 1 ELSE 0 END) t_uscita_c_priv,
	SUM(CASE WHEN id_tipo_conto = 3 and segno = '-' THEN 1 ELSE 0 END) t_uscita_c_fam,
	SUM(CASE WHEN id_tipo_conto = 0 and segno = '+' THEN 1 ELSE 0 END) t_entrata_c_base,
	SUM(CASE WHEN id_tipo_conto = 1 and segno = '+' THEN 1 ELSE 0 END) t_entrata_c_business,
	SUM(CASE WHEN id_tipo_conto = 2 and segno = '+' THEN 1 ELSE 0 END) t_entrata_c_priv,
	SUM(CASE WHEN id_tipo_conto = 3 and segno = '+' THEN 1 ELSE 0 END) t_entrata_c_fam,
	SUM(CASE WHEN id_tipo_conto = 0 and segno = '-' THEN importo ELSE 0 END) imp_uscita_c_base,
	SUM(CASE WHEN id_tipo_conto = 1 and segno = '-' THEN importo ELSE 0 END) imp_uscita_c_business,
	SUM(CASE WHEN id_tipo_conto = 2 and segno = '-' THEN importo ELSE 0 END) imp_uscita_c_priv,
	SUM(CASE WHEN id_tipo_conto = 3 and segno = '-' THEN importo ELSE 0 END) imp_uscita_c_fam,
	SUM(CASE WHEN id_tipo_conto = 0 and segno = '+' THEN importo ELSE 0 END) imp_entrata_c_base,
	SUM(CASE WHEN id_tipo_conto = 1 and segno = '+' THEN importo ELSE 0 END) imp_entrata_c_business,
	SUM(CASE WHEN id_tipo_conto = 2 and segno = '+' THEN importo ELSE 0 END) imp_entrata_c_priv,
	SUM(CASE WHEN id_tipo_conto = 3 and segno = '+' THEN importo ELSE 0 END) imp_entrata_c_fam
	FROM conti_info c
	LEFT JOIN transazioni_info t
	ON c.id_conto=t.id_conto
	GROUP BY 1;

SELECT * FROM trans_per_cliente_per_conto; /*visualizzo tabella creata*/


/* creo tabella temporanea per aggregazioni su transazioni totali per cliente*/
DROP TABLE IF EXISTS trans_tot_per_cliente;
CREATE TEMPORARY TABLE trans_tot_per_cliente AS
	SELECT 
	c.id_cliente, c.eta,
	SUM(CASE WHEN n_trans_tot IS NULL THEN 0 ELSE n_trans_tot END) n_trans_tot,
	SUM(CASE WHEN trans_entrata IS NULL THEN 0 ELSE trans_entrata END) n_trans_entrata,
	SUM(CASE WHEN trans_uscita IS NULL THEN 0 ELSE trans_uscita END) n_trans_uscita,
	SUM(CASE WHEN importo_entrata IS NULL THEN 0 ELSE importo_entrata END) imp_entrata_tot,
	SUM(CASE WHEN importo_uscita IS NULL THEN 0 ELSE importo_uscita END) imp_uscita_tot
	FROM conti_info c
	LEFT JOIN trans_per_conto t
	ON c.id_conto=t.id_conto
	GROUP BY 1,2;

SELECT * FROM trans_tot_per_cliente; /*visualizzo tabella creata*/


/* creo tabella finale 
denormalizzata per cliente con dati su conti, transazioni e tipi di conto*/

DROP TABLE IF EXISTS banca.analisi_transazioni_clienti;  /*pulisco se ci fosse già una tabella con questo nome*/

CREATE TABLE banca.analisi_transazioni_clienti AS
	SELECT ttpc.*,
	cpc.num_conti_tot, cpc.num_conti_base, cpc.num_conti_business, cpc.num_conti_priv, cpc.num_conti_fam,
	tpcpc.t_uscita_c_base, tpcpc.t_uscita_c_business, tpcpc.t_uscita_c_priv, tpcpc.t_uscita_c_fam, 
	tpcpc.t_entrata_c_base, tpcpc.t_entrata_c_business, tpcpc.t_entrata_c_priv, tpcpc.t_entrata_c_fam, 
	tpcpc.imp_uscita_c_base, tpcpc.imp_uscita_c_business, tpcpc.imp_uscita_c_priv, tpcpc.imp_uscita_c_fam, 
	tpcpc.imp_entrata_c_base, tpcpc.imp_entrata_c_business, tpcpc.imp_entrata_c_priv, tpcpc.imp_entrata_c_fam
	FROM conti_per_cliente cpc
	INNER JOIN trans_tot_per_cliente ttpc
	ON cpc.id_cliente=ttpc.id_cliente

	INNER JOIN trans_per_cliente_per_conto tpcpc
	ON cpc.id_cliente=tpcpc.id_cliente

	ORDER BY id_cliente;
    
    
SELECT * FROM banca.analisi_transazioni_clienti; /*visualizzo tabella creata*/
