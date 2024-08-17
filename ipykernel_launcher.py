import pubchempy as pcp

def get_compound_info(cid):
    try:
        # CID를 이용해 화합물 정보 가져오기
        compound = pcp.get_compounds(cid, 'cid')[0]
        
        # 분자량, 이름, 분자식 추출
        molecular_weight = compound.molecular_weight
        name = compound.iupac_name if compound.iupac_name else compound.synonyms[0]  # IUPAC 이름이 있으면 사용, 없으면 Synonym 사용
        molecular_formula = compound.molecular_formula

        return molecular_weight, name, molecular_formula
    except Exception as e:
        print(f"Error retrieving information for CID {cid}: {e}")
        return None, None, None

# CID 3에 대한 정보 조회
cid = 3
molecular_weight, name, molecular_formula = get_compound_info(cid)

if molecular_weight and name and molecular_formula:
    print(f"Compound Name: {name}")
    print(f"Molecular Formula: {molecular_formula}")
    print(f"Molecular Weight: {molecular_weight} g/mol")
else:
    print(f"Failed to retrieve information for CID {cid}.")