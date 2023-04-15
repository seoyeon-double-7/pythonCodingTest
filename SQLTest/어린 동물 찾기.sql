-- 코드를 입력하세요
-- SELECT ANIMAL_ID, NAME from animal_ins WHERE not INTAKE_CONDITION = 'Aged' ORDER BY ANIMAL_ID;

--SELECT ANIMAL_ID, NAME from animal_ins WHERE INTAKE_CONDITION != 'Aged' ORDER BY ANIMAL_ID;

SELECT ANIMAL_ID, NAME from animal_ins WHERE INTAKE_CONDITION Not in('Aged') ORDER BY ANIMAL_ID;