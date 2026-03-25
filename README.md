> [!NOTE]
> 
> This repository is no longer updated. 
> Please refer to the latest PSF models at the MIDIS data release webpage on [Zenodo](https://doi.org/10.5281/zenodo.15535600).
> 
> If you use these PSF models, please cite [Boogaard et al. 2024](https://ui.adsabs.harvard.edu/abs/2024ApJ...969...27B/abstract) as well as [Östlin et al. 2025](https://ui.adsabs.harvard.edu/abs/2025A%26A...696A..57O/abstract).

# midis_psf
The MIRI Deep Imaging Survey (MIDIS) Point Spread Function (PSF)
model.  For details, please refer to Appendix A of [Boogaard et
al. 2024](https://ui.adsabs.harvard.edu/abs/2024ApJ...969...27B/abstract).

The empirical PSF models that were used to construct these PSFs can be
found at https://github.com/jensmelinder/miripsfs.

If you use either of the above PSF models, please cite [Boogaard et
al. 2024](https://ui.adsabs.harvard.edu/abs/2024ApJ...969...27B/abstract).

## Usage

On the command line:
``` shell
midis_psf.py 53.1751187 -27.7665497 -fTrue -p60  # return psf filename only (default), at 60mas (default)
midis_psf.py 0 0 -i5 -p40                        # return psf number 5 at 40mas (coordinates are superseded by -i)
```

In python:
``` python
import midis_psf
psf = midis_psf.get_psf(53.1751187, -27.7665497, filename_only=False, pixscale=30)   # returns psf at coords, 30mas
psf = midis_psf.get_psf(0, 0, 5, filename_only=False, pixscale=40)                   # returns psf no. 5, at 40mas
```

## The Data
![psf_map](data-v5/map_psf.png)
![psf_tmpl](data-v5/60mas/psf9-recovered-v5-60mas.png)
