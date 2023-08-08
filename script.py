query = {
    "StmBairro" : "SELECT baicod, bainom FROM public.arr_bai",
    "StmEmpresa" : """SELECT 
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
                        left join public.arr_mun1 m2 on (m2.muncod = p.conmuncod) """,
    "StmEmpresaSituacao":""" """
}