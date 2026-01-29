# anaconda(또는 miniconda)가 존재하지 않을 경우 설치해주세요!
## TODO

if ! command -v conda >/dev/null 2>&1; then
    CONDA_DIR=$HOME/miniconda3
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O Miniconda3.sh
    bash Miniconda3.sh -b -p $CONDA_DIR
    rm -f Miniconda3.sh
    export PATH="$HOME/miniconda3/bin:$PATH"
fi

CONDA_BASE="$(conda info --base)"
source $CONDA_BASE/etc/profile.d/conda.sh

# Conda 환셩 생성 및 활성화
## TODO

# ToS bug fix
export CONDA_PLUGINS_AUTO_ACCEPT_TOS=yes

conda create --name myenv python=3.11 -y
conda activate myenv

## 건드리지 마세요! ##
python_env=$(python -c "import sys; print(sys.prefix)")
if [[ "$python_env" == *"/envs/myenv"* ]]; then
    echo "[INFO] 가상환경 활성화: 성공"
else
    echo "[INFO] 가상환경 활성화: 실패"
    exit 1 
fi

# 필요한 패키지 설치
## TODO
pip install mypy

# Submission 폴더 파일 실행

SUBMISSION_DIR="submission"
MAIN_DIR="../"
INPUT_DIR="$MAIN_DIR/input"
OUTPUT_DIR="$MAIN_DIR/output"

cd "$SUBMISSION_DIR" || { echo "[INFO] submission 디렉토리로 이동 실패"; exit 1; }

for file in *.py; do
    ## TODO
    id="${file#*_}"
    id="${id%.py}"
    python $file < "$INPUT_DIR/${id}_input" > "$OUTPUT_DIR/${id}_output" 

done

# mypy 테스트 실행 및 mypy_log.txt 저장
## TODO
mypy . > mypy_log.txt
rm -rf .mypy_cache

# conda.yml 파일 생성
## TODO
conda env export > conda.yml

# 가상환경 비활성화
## TODO
conda deactivate
