query = {
    "StmBairro": "SELECT baicod, bainom FROM public.arr_bai",
    "StmEmpresa": """SELECT 
                        regexp_replace(p.concpfcnpj, '[\.\-\/\s]', '', 'g') as nrcnpj,
                        e.bcecod as nrinscricaoempresa,
                        'nrnaturezajuridica' as nrnaturezajuridica,
                        1 as tpimovelempresa, --1 - Imóvel Urbano
                        '' as nrimovelurbano,
                        '' as nrimovelrural,
                        'nrcpfprofissionalcontabil' as nrcpfprofissionalcontabil,
                        'nrempregados' as nrempregados,
                        e.bceareuti as qtareautilizada,
                        e.bcesimpnac as tpopcaosimples,
                        TO_CHAR(e.bcesimpnacdat, 'DD/MM/YYYY') as dtenquadramentosimples,
                        'dtexclusaosimples' as dtexclusaosimples,
                        'issedeprincipal' as issedeprincipal, --1 - SIM | 2 - NÃO
                        'isPermiteMultiplasSedes' as isPermiteMultiplasSedes, --1 - SIM | 2 - NÃO
                        trim(e.bceruanom) as dsEnderecoCorresp,
                        coalesce(trim(e.bceruanum), 'S/N') as nrResidencialCorresp,
                        substring(e.bceruacom from 1 for 20) as dscomplementocorresp,
                        trim(b.bainom) as dsBairroCorresp,
                        substring (m.munnom from 1 for 30),
                        m.munuf as dsufcorresp,
                        regexp_replace(e.bcecep, '^\d{8}$', '', 'g') as nrCepCorresp,
                        'isSubstitutoTributario' as isSubstitutoTributario,  --1 - SIM | 2 - NÃO
                        --coalesce('nmunidadmin' from 1 for 60) as nmunidadmin,
                        case e.bceregesptrib
                            when 5 then 1 --'Optante do MEI sim-1'
                            Else '2' end tpOpcaoMei,
                        TO_CHAR(e.bceregesptribdat, 'DD/MM/YYYY') as dtenquadramentomei,
                        'dtexclusaomei' as dtexclusaomei,
                        'tpCaractEmpresaSede' as tpCaractEmpresaSede,
                        'tpSituacaoFisicaEmpresa' as tpSituacaoFisicaEmpresa,
                        'tpTipoImovelEmpresa' as tpTipoImovelEmpresa,
                        p.conend as dsEndereco,
                        coalesce(trim(p.connum),'S/N') as nrResidencial,
                        substring(trim(p.concom) from 1 for 20) as dscomplemento,
                        trim(p.conbai) as dsBairro,
                        regexp_replace(p.concep, '^\d{8}$', '', 'g') as nrCep,
                        substring (trim(m2.munnom) from 1 for 30) as dsMunicipio,
                        p.conmunuf as dsuf,
                        3 as tpEnderecoEmpresa, --1 - Endereço CNPJ | 2 - Endereço inscrição | 3 - Outro
                        99 as idhorario, -- 1=Geral | 2=Horário Especial | 99=Comercial | 100=Sem Horário especifico
                        trim(regexp_replace(e.bceativ, '\s+', ' ', 'g'))
                        FROM public.arr_bce e
                        join public.arr_con p on (p.concod = e.bceconcod)
                        left join public.arr_bai b on (b.baicod = e.bcebaicod)
                        left join public.arr_mun1 m on (m.muncod = e.bcemuncod)
                        left join public.arr_mun1 m2 on (m2.muncod = p.conmuncod)
                        where p.conmuncod = 4127304 """,
    "StmEmpresaSituacao": """ SELECT 
                        regexp_replace(p.concpfcnpj, '[\.\-\/\s]', '', 'g') as nrcnpj,
                        e.bcecod as nrinscricaoempresa,
                        case e.bcesituacao 
                            when 1 then 2
                            when 2 then 4
                            when 0 then 4 else 1 end as stempresa, --1, "Pré Cadastro | 2 - Ativa [1] | 3 - Inativa - Paralisada | 4 - Baixada [2][0]| 5 - Temporário
                        coalesce(TO_CHAR(e.bcedatalt, 'DD/MM/YYYY'),TO_CHAR(e.bcedatcad, 'DD/MM/YYYY')) as dtaltempresasituacao,
                        '' as nrprocessoaltempresa
                        FROM public.arr_bce e
                        left join public.arr_con p on (p.concod = e.bceconcod)
                        where p.conmuncod = 4127304 """,
    "StmEmpresaFora": """ SELECT
                        regexp_replace(p.concpfcnpj, '[.\-/\s]', '', 'g') as nrcnpj,
                        e.bcecod as nrinscricaoempresafora,
                        e.bcesimpnac as tpopcaosimplesempfora,
                        'nrnaturezajuridica' as nrnaturezajuridica,
                        'isSubstitutoTributario' as issubstitutotributariofora, --1 - SIM | 2 - NÃO
                        substring(ps.paisnom from 1 for 80) as pais
                        FROM public.arr_bce e
                        join public.arr_con p on (p.concod = e.bceconcod)
                        left join public.arr_bai b on (b.baicod = e.bcebaicod)
                        left join public.arr_mun1 m on (m.muncod = e.bcemuncod)
                        left join public.arr_pais ps on (ps.paiscod = p.paiscod)
                        where p.conmuncod != 4127304 """,
    "StmEmpresaForaSituacao": """ SELECT
                            regexp_replace(p.concpfcnpj, '[.\-/\s]', '', 'g') as nrcnpj,
                            e.bcecod as nrinscricaoempresafora,
                            coalesce(TO_CHAR(e.bcedatalt, 'DD/MM/YYYY'),TO_CHAR(e.bcedatcad, 'DD/MM/YYYY')) as dtaltsitempfora,
                            case e.bcesituacao 
                                when 1 then 2
                                when 2 then 4
                                when 0 then 4 else 1 end as stempresa --1, "Pré Cadastro | 2 - Ativa [1] | 3 - Inativa - Paralisada | 4 - Baixada [2][0]| 5 - Temporário
                            FROM public.arr_bce e
                            left join public.arr_con p on (p.concod = e.bceconcod)
                            where p.conmuncod != 4127304 """,
    "StmEmpresaForaAtividade": """ SELECT
                                regexp_replace(p.concpfcnpj, '[-./\s]', '', 'g') as nrcnpj,
                                e.bcecod as nrinscricaoempresafora,
                                '' as nrsubclasse
                                FROM public.arr_bce e
                                left join public.arr_con p on (p.concod = e.bceconcod)
                                where p.conmuncod != 4127304 """,
    "StmEmpresaServico": """ select
                        e.bcecod as nrmatriculaempresa,
                        right(i.servitemcodmun, 2) as nrservicoaesubitem,
                        left(i.servitemcodmun, 2) as nrservicoaeitem,
                        'istomadorobrigatorio' as istomadorobrigatorio, --1 - SIM | 2 - NÃO) - Not Null
                        'ispermiteisentoimune' as ispermiteisentoimune, --1 - SIM | 2 - NÃO) - Not Null
                        'istributaemoutromunicipio' as istributaemoutromunicipio --1 - SIM | 2 - NÃO
                        from arr_bce e
                        join arr_bce8 s on (s.bcecod=e.bcecod)
                        join arr_servitem i on (i.servitemcod=s.bceservitemcod) """



}