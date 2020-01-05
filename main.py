from imports import *
from utils import *
from nicer import NICER
import config

if __name__ == '__main__':
    running_in_container = True if os.environ.get('RUNNING_IN_CONTAINER') else False
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    img_dir = '/autofs/ceph-stud/fischer/thesis/eval_gui/tmp'

    nima_path = r'C:\Users\Michi\Downloads\epoch-57.pkl'
    nicer = NICER(checkpoint_can=config.can_checkpoint_path, checkpoint_nima=config.nima_checkpoint_path, device=device)

    #nicer.enhance_image_folder(img_dir)
    enh_img, init_nima, final_nima = nicer.enhance_image(r'C:\Users\Michi\Downloads\unedited\corrected\img3860.jpg')
    pil_img = Image.fromarray(enh_img)
    print("Saving...")
    pil_img.save(r'C:\Users\Michi\Downloads\nima_imgs\img3860_enhanced_new.jpg')
