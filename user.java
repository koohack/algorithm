import sun.rmi.server.InactiveGroupException;

import java.util.ArrayList;

class UserSolution {

    static ArrayList<Integer> grade1ID = new ArrayList<Integer>();
    static ArrayList<Integer> grade1Gen = new ArrayList<Integer>();
    static ArrayList<Integer> grade1Sco = new ArrayList<Integer>();

    static ArrayList<Integer> grade2ID = new ArrayList<Integer>();
    static ArrayList<Integer> grade2Gen = new ArrayList<Integer>();
    static ArrayList<Integer> grade2Sco = new ArrayList<Integer>();

    static ArrayList<Integer> grade3ID = new ArrayList<Integer>();
    static ArrayList<Integer> grade3Gen = new ArrayList<Integer>();
    static ArrayList<Integer> grade3Sco = new ArrayList<Integer>();

    public void init() {
        grade1ID = new ArrayList<Integer>();
        grade1Gen = new ArrayList<Integer>();
        grade1Sco = new ArrayList<Integer>();

        grade2ID = new ArrayList<Integer>();
        grade2Gen = new ArrayList<Integer>();
        grade2Sco = new ArrayList<Integer>();

        grade3ID = new ArrayList<Integer>();
        grade3Gen = new ArrayList<Integer>();
        grade3Sco = new ArrayList<Integer>();
    }

    public static int findmx(int gender, ArrayList<Integer> ids, ArrayList<Integer> genders, ArrayList<Integer> scores){
        int length = ids.size();

        int mx = 0;
        int mnID = 0;

        for (int i = 0; i < length; i++) {
            if (genders.get(i) == gender){
                if (mx < scores.get(i)){
                    mx = scores.get(i);
                    mnID = ids.get(i);
                }else if (mx == scores.get(i)){
                    if (mnID < ids.get(i)){
                        mnID = ids.get(i);
                    }
                }
            }
        }
        return mnID;
    }

    public int add(int mId, int mGrade, char mGender[], int mScore) {
        int gender = 0;
        if (mGender[0] == 'm') gender = 0;
        else gender = 1;

        int ret = 0;

        if (mGrade == 1){
            grade1ID.add(mId);
            grade1Sco.add(mScore);
            grade1Gen.add(gender);
            ret = findmx(gender, grade1ID, grade1Gen, grade1Sco);
        }else if (mGrade == 2){
            grade2ID.add(mId);
            grade2Sco.add(mScore);
            grade2Gen.add(gender);
            ret = findmx(gender, grade2ID, grade2Gen, grade2Sco);
        }else{
            grade3ID.add(mId);
            grade3Sco.add(mScore);
            grade3Gen.add(gender);
            ret = findmx(gender, grade3ID, grade3Gen, grade3Sco);
        }

        return ret;
    }

    public int remove(int mId) {
        int[] idIndex = {-1, -1, -1};
        int grade = 0;
        int ret = 0;
        int gender = 0;

        // 1
        int length1 = grade1ID.size();
        for (int i = 0; i < length1; i++) {
            if (grade1ID.get(i) == mId){
                idIndex[0] = i;
                grade = 1;
                break;
            }
        }

        // 2
        int length2 = grade2ID.size();
        for (int i = 0; i < length2; i++) {
            if (grade2ID.get(i) == mId){
                idIndex[1] = i;
                grade = 2;
                break;
            }
        }

        // 3
        int length3 = grade3ID.size();
        for (int i = 0; i < length3; i++) {
            if (grade3ID.get(i) == mId){
                idIndex[2] = i;
                grade = 3;
                break;
            }
        }
        if (grade == 0){
            return 0;
        }

        // remove and get gender
        int ind = idIndex[grade-1];
        if (grade == 1){
            grade1ID.remove(ind);
            gender = grade1Gen.remove(ind);
            grade1Sco.remove(ind);
        }else if (grade == 2){
            grade2ID.remove(ind);
            gender = grade2Gen.remove(ind);
            grade2Sco.remove(ind);
        }else{
            grade3ID.remove(ind);
            gender = grade3Gen.remove(ind);
            grade3Sco.remove(ind);
        }

        // get mn
        int mn = 1000000000;
        int mnIndex = 1000000001;

        if (grade == 1){
            int length = grade1ID.size();
            for (int i = 0; i < length; i++) {
                if (grade1Gen.get(i) == gender && grade1Sco.get(i) < mn){
                    mn = grade1Sco.get(i);
                    mnIndex = grade1ID.get(i);
                }else if (grade1Gen.get(i) == gender && grade1Sco.get(i) == mn){
                    if (mnIndex > grade1ID.get(i)){
                        mnIndex = grade1ID.get(i);
                    }
                }
            }
        }else if (grade == 2){
            int length = grade2ID.size();
            for (int i = 0; i < length; i++) {
                if (grade2Gen.get(i) == gender && grade2Sco.get(i) < mn){
                    mn = grade2Sco.get(i);
                    mnIndex = grade2ID.get(i);
                }else if (grade2Gen.get(i) == gender && grade2Sco.get(i) == mn){
                    if (mnIndex > grade2ID.get(i)){
                        mnIndex = grade2ID.get(i);
                    }
                }
            }
        }else{
            int length = grade3ID.size();
            for (int i = 0; i < length; i++) {
                if (grade3Gen.get(i) == gender && grade3Sco.get(i) < mn){
                    mn = grade3Sco.get(i);
                    mnIndex = grade3ID.get(i);
                }else if (grade3Gen.get(i) == gender && grade3Sco.get(i) == mn){
                    if (mnIndex > grade3ID.get(i)){
                        mnIndex = grade3ID.get(i);
                    }
                }
            }
        }

        if (mnIndex == 1000000001){
            return 0;
        }else{
            return mnIndex;
        }
    }

    public int query(int mGradeCnt, int mGrade[], int mGenderCnt, char mGender[][], int mScore) {
        int mn = 1000000000;
        int mnID = 1000000001;

        int ret = 0;

        for (int i = 0; i < mGradeCnt; i++) {
            int grade = mGrade[i];
            for (int j = 0; j < mGenderCnt; j++) {
                int gender = 0;
                char[] g = mGender[j];
                if (g[0] == 'm'){
                    gender = 0;
                }else{
                    gender = 1;
                }

                if (grade == 1){
                    int length = grade1ID.size();
                    for (int k = 0; k < length; k++) {
                        if (grade1Gen.get(k) == gender && grade1Sco.get(k) < mn && grade1Sco.get(k) >= mScore){
                            mn = grade1Sco.get(k);
                            mnID = grade1ID.get(k);
                        }else if (grade1Gen.get(k) == gender && grade1Sco.get(k) == mn && grade1Sco.get(k) >= mScore){
                            if (mnID > grade1ID.get(k)){
                                mnID = grade1ID.get(k);
                            }
                        }
                    }
                }else if (grade == 2){
                    int length = grade2ID.size();
                    for (int k = 0; k < length; k++) {
                        if (grade2Gen.get(k) == gender && grade2Sco.get(k) < mn && grade2Sco.get(k) >= mScore){
                            mn = grade2Sco.get(k);
                            mnID = grade2ID.get(k);
                        }else if (grade2Gen.get(k) == gender && grade2Sco.get(k) == mn && grade2Sco.get(k) >= mScore){
                            if (mnID > grade2ID.get(k)){
                                mnID = grade2ID.get(k);
                            }
                        }
                    }
                }else{
                    int length = grade3ID.size();
                    for (int k = 0; k < length; k++) {
                        if (grade3Gen.get(k) == gender && grade3Sco.get(k) < mn && grade3Sco.get(k) >= mScore){
                            mn = grade3Sco.get(k);
                            mnID = grade3ID.get(k);
                        }else if (grade3Gen.get(k) == gender && grade3Sco.get(k) == mn && grade3Sco.get(k) >= mScore){
                            if (mnID > grade3ID.get(k)){
                                mnID = grade3ID.get(k);
                            }
                        }
                    }
                }
            }
        }

        if (mnID == 1000000001){
            return 0;
        }else{
            return mnID;
        }
    }
}